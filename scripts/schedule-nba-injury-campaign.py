# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

def get_token():
    t = os.environ.get('BUFFER_ACCESS_TOKEN')
    if t:
        return t
    for env_name in ['.env.local', '.env']:
        p = os.path.join(os.path.dirname(__file__), '..', env_name)
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('BUFFER_ACCESS_TOKEN='):
                        val = line.strip().split('=', 1)[1].strip()
                        if val:
                            return val
    return 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0'

TOKEN = get_token()
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn Channel ID

def verify_prod_assets(queue):
    print("Pre-flight Probe: Checking NBA Injury assets on production domain...")
    ctx = ssl._create_unverified_context()
    failed = []
    
    for item in queue:
        url = item['cdnUrl']
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                if resp.status != 200:
                    failed.append((url, resp.status))
                else:
                    print(f"  [200 OK] {item['imageFilename']}")
        except Exception as e:
            failed.append((url, str(e)))
            
    if failed:
        print(f"\n[ALERT] Pre-flight probe failed for {len(failed)} assets: {failed}")
        return False
    print("\nPre-flight Probe PASSED: All 8 NBA Injury assets are returning HTTP 200 OK!\n")
    return True

def schedule_posts():
    queue_file = os.path.join(os.path.dirname(__file__), 'master-nba-injury-queue.json')
    with open(queue_file, 'r', encoding='utf-8') as f:
        queue = json.load(f)
        
    print(f"Loaded NBA injury master queue with {len(queue)} posts.")
    
    if not verify_prod_assets(queue):
        print("HALTING: Assets not yet live on production. Please deploy to Vercel first.")
        return False

    report_path = os.path.join(os.path.dirname(__file__), 'nba-injury-scheduled-report.json')
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    if item.get('status') in ['scheduled', 'success'] and item.get('postId'):
                        results[item['postIndex']] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    graphql_url = "https://api.buffer.com"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    ctx = ssl._create_unverified_context()
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            status
            dueAt
          }
        }
        ... on LimitReachedError {
          message
        }
        ... on InvalidInputError {
          message
        }
        ... on UnexpectedError {
          message
        }
        ... on UnauthorizedError {
          message
        }
      }
    }
    """

    for i, p in enumerate(queue, 1):
        p_idx = p["postIndex"]
        if p_idx in results and results[p_idx].get("postId"):
            print(f"[{i}/{len(queue)}] Post #{p_idx} already scheduled (Buffer ID: {results[p_idx]['postId']}). Skipping.")
            continue

        retries = 0
        while retries < 5:
            print(f"\n[{i}/{len(queue)}] Scheduling NBA Injury Post #{p_idx} ({p['scheduledDate']} - {p['slotType']})...")
            print(f"  Asset: {p['cdnUrl']}")
            print(f"  Headline: {p['headline']}")

            payload = {
                "query": mutation,
                "variables": {
                    "input": {
                        "channelId": CHANNEL_ID,
                        "text": p["caption"],
                        "schedulingType": "automatic",
                        "mode": "customScheduled",
                        "dueAt": p["scheduledAt"],
                        "saveToDraft": False,
                        "needsApproval": False,
                        "assets": [
                            {
                                "image": {
                                    "url": p["cdnUrl"]
                                }
                            }
                        ]
                    }
                }
            }

            req = urllib.request.Request(graphql_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    errors = res_data.get("errors")
                    if errors:
                        print(f"  >>> GRAPHQL ERROR: {errors}")
                        p["status"] = "failed"
                        p["error"] = errors[0].get("message")
                        results[p_idx] = p
                        break
                    else:
                        create_res = res_data.get("data", {}).get("createPost", {})
                        if "post" in create_res and create_res["post"].get("id"):
                            post_id = create_res["post"]["id"]
                            st = create_res["post"].get("status")
                            due = create_res["post"].get("dueAt")
                            p["status"] = st
                            p["postId"] = post_id
                            p["dueAt"] = due
                            print(f"  >>> SUCCESS: Post ID: {post_id} (Status: {st})")
                            results[p_idx] = p
                            break
                        else:
                            err_msg = create_res.get("message", "Unknown error")
                            print(f"  >>> ERROR: {err_msg}")
                            p["status"] = "failed"
                            p["error"] = err_msg
                            results[p_idx] = p
                            if "limit" in err_msg.lower():
                                print("Daily buffer queue limit reached. Saving progress.")
                                with open(report_path, "w", encoding="utf-8") as rf:
                                    json.dump(list(results.values()), rf, indent=2, ensure_ascii=False)
                                return False
                            break
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    retries += 1
                    retry_after = he.headers.get('Retry-After')
                    wait_sec = int(retry_after) if retry_after and retry_after.isdigit() else 60
                    print(f"  [RATE LIMIT 429] Waiting {wait_sec + 5}s (Attempt {retries}/5)...")
                    time.sleep(wait_sec + 5)
                    continue
                err_body = he.read().decode("utf-8", errors="replace")
                print(f"  >>> HTTP ERROR {he.code}: {err_body}")
                p["status"] = "failed"
                p["error"] = f"HTTP {he.code}: {err_body}"
                results[p_idx] = p
                break
            except Exception as e:
                print(f"  >>> NETWORK ERROR: {e}")
                p["status"] = "failed"
                p["error"] = str(e)
                results[p_idx] = p
                break

        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as rf:
        json.dump(list(results.values()), rf, indent=2, ensure_ascii=False)
    
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"] and r.get("postId"))
    print(f"\nExecution complete. Successfully scheduled {success_count}/{len(queue)} NBA Injury posts to Buffer.")
    return success_count == len(queue)

if __name__ == "__main__":
    schedule_posts()
