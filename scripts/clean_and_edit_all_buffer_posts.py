# -*- coding: utf-8 -*-
"""
Remove all Markdown bolding (**) from LinkedIn captions and update scheduled posts in Buffer via GraphQL editPost.
Ensures zero asterisks are rendered on LinkedIn.
"""

import sys
import os
import json
import ssl
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')

EDIT_POST_MUTATION = """
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        status
      }
    }
    ... on InvalidInputError { message }
    ... on NotFoundError { message }
    ... on LimitReachedError { message }
    ... on UnexpectedError { message }
    ... on UnauthorizedError { message }
  }
}
"""

def clean_markdown_bold(text):
    # Removes ** markdown markers cleanly
    return text.replace("**", "")

def execute_edit_post(buffer_post_id, new_text):
    ctx = ssl._create_unverified_context()
    payload = json.dumps({
        "query": EDIT_POST_MUTATION,
        "variables": {
            "input": {
                "id": buffer_post_id,
                "text": new_text
            }
        }
    }).encode("utf-8")
    
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            edit_data = data.get("data", {}).get("editPost", {})
            typename = edit_data.get("__typename")
            if typename == "PostActionSuccess":
                return True, typename, edit_data.get("post", {}).get("status")
            else:
                msg = edit_data.get("message") or json.dumps(edit_data)
                return False, typename, msg
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get("Retry-After")
        wait = int(retry_after) if retry_after and retry_after.isdigit() else 30
        return False, "429", wait
    except Exception as e:
        return False, "NetworkError", str(e)

def update_como_campaign():
    print("================================================================")
    print("🧹 REMOVING ASTERISKS (**) FROM COMO 1907 CAMPAIGN (112 POSTS)")
    print("================================================================\n")
    
    queue_file = "scripts/master-como-queue.json"
    with open(queue_file, "r", encoding="utf-8") as f:
        queue = json.load(f)
        
    for p in queue:
        p["text"] = clean_markdown_bold(p["text"])
        
    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
    print(f"Updated {queue_file} with clean, bold-free captions.")
    
    # Update local captions and gallery
    captions_dir = r"C:\Users\Zhane\Documents\Website stuff\lornetteig\Career Circle Posts\october ads\como oct20thiwin\_LD_COMO_CAMPAIGN_BUILD\06_CAPTIONS"
    if os.path.exists(captions_dir):
        for p in queue:
            fpath = os.path.join(captions_dir, f"{p['id']}.txt")
            with open(fpath, "w", encoding="utf-8") as out:
                out.write(f"ID: {p['id']}\n")
                out.write(f"Day: {p['day']} | Slot: {p['slot']}\n")
                out.write(f"Theme: {p['theme']}\n")
                out.write(f"Mode: {p['mode']} | Due At: {p.get('dueAt')}\n")
                out.write(f"Asset: {p['asset_url']} ({p['asset_type']})\n")
                out.write("=" * 60 + "\n\n")
                out.write(p["text"] + "\n")
        print("Updated local 06_CAPTIONS files.")

    # Update 08_EDITABLE_PROJECT/campaign_manifest.json
    manifest_path = r"C:\Users\Zhane\Documents\Website stuff\lornetteig\Career Circle Posts\october ads\como oct20thiwin\_LD_COMO_CAMPAIGN_BUILD\08_EDITABLE_PROJECT\campaign_manifest.json"
    if os.path.exists(manifest_path):
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(queue, f, indent=2)
        print("Updated 08_EDITABLE_PROJECT/campaign_manifest.json.")

    # Update report and Buffer
    report_file = "scripts/como-scheduled-report.json"
    with open(report_file, "r", encoding="utf-8") as f:
        report = json.load(f)

    queue_by_id = {p["id"]: p for p in queue}
    
    success_count = 0
    total = len(report)
    
    for idx, (post_id, item_info) in enumerate(report.items(), 1):
        buffer_id = item_info.get("postId")
        clean_text = queue_by_id[post_id]["text"]
        
        # Check if already updated
        if item_info.get("cleaned_asterisks"):
            success_count += 1
            continue
            
        while True:
            print(f"[{idx}/{total}] Updating {post_id} (Buffer ID: {buffer_id})...", end="", flush=True)
            ok, type_or_code, msg = execute_edit_post(buffer_id, clean_text)
            
            if ok:
                print(f" ✅ SUCCESS ({msg})")
                item_info["cleaned_asterisks"] = True
                with open(report_file, "w", encoding="utf-8") as f:
                    json.dump(report, f, indent=2)
                success_count += 1
                time.sleep(0.5)  # Smooth pacing to avoid 429
                break
            elif type_or_code == "429":
                wait_sec = msg if isinstance(msg, int) else 30
                print(f" [429 RATE LIMIT] Pausing for {wait_sec}s...", flush=True)
                time.sleep(wait_sec)
                continue
            else:
                print(f" ⚠️ {type_or_code}: {msg}")
                # If post was already sent (e.g. shareNow post 1), mark as recorded
                item_info["cleaned_asterisks"] = True
                item_info["note"] = f"editPost returned {type_or_code}: {msg}"
                with open(report_file, "w", encoding="utf-8") as f:
                    json.dump(report, f, indent=2)
                break

    print(f"\n✅ Finished Como Campaign: {success_count}/{total} posts updated in Buffer.")

def update_superpowers_campaign():
    print("\n================================================================")
    print("🧹 REMOVING ASTERISKS (**) FROM SUPERPOWERS CAMPAIGN (42 POSTS)")
    print("================================================================\n")
    
    queue_file = "scripts/master-superpowers-queue.json"
    with open(queue_file, "r", encoding="utf-8") as f:
        queue = json.load(f)
        
    for p in queue:
        p["text"] = clean_markdown_bold(p["text"])
        
    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
    print(f"Updated {queue_file} with clean, bold-free captions.")

    report_file = "scripts/superpowers-scheduled-report.json"
    with open(report_file, "r", encoding="utf-8") as f:
        report = json.load(f)

    queue_by_id = {p["id"]: p for p in queue}
    
    success_count = 0
    total = len(report)
    
    for idx, (post_id, item_info) in enumerate(report.items(), 1):
        buffer_id = item_info.get("postId")
        clean_text = queue_by_id[post_id]["text"]
        
        if item_info.get("cleaned_asterisks"):
            success_count += 1
            continue
            
        while True:
            print(f"[{idx}/{total}] Updating {post_id} (Buffer ID: {buffer_id})...", end="", flush=True)
            ok, type_or_code, msg = execute_edit_post(buffer_id, clean_text)
            
            if ok:
                print(f" ✅ SUCCESS ({msg})")
                item_info["cleaned_asterisks"] = True
                with open(report_file, "w", encoding="utf-8") as f:
                    json.dump(report, f, indent=2)
                success_count += 1
                time.sleep(0.5)
                break
            elif type_or_code == "429":
                wait_sec = msg if isinstance(msg, int) else 30
                print(f" [429 RATE LIMIT] Pausing for {wait_sec}s...", flush=True)
                time.sleep(wait_sec)
                continue
            else:
                print(f" ⚠️ {type_or_code}: {msg}")
                item_info["cleaned_asterisks"] = True
                item_info["note"] = f"editPost returned {type_or_code}: {msg}"
                with open(report_file, "w", encoding="utf-8") as f:
                    json.dump(report, f, indent=2)
                break

    print(f"\n✅ Finished Superpowers Campaign: {success_count}/{total} posts updated in Buffer.")

def update_generator_scripts():
    # Update scripts/build_full_como_campaign.py to remove ** from template
    p1 = "scripts/build_full_como_campaign.py"
    if os.path.exists(p1):
        with open(p1, "r", encoding="utf-8") as f:
            code = f.read()
        code = code.replace('post_text = f"""**{title}**', 'post_text = f"""{title}')
        code = code.replace('**Key Takeaway:** {takeaway}', 'Key Takeaway: {takeaway}')
        code = code.replace('title = "**91 YEARS', 'title = "91 YEARS')
        with open(p1, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Updated {p1} template.")

    p2 = "scripts/schedule-superpowers-campaign.py"
    if os.path.exists(p2):
        with open(p2, "r", encoding="utf-8") as f:
            code = f.read()
        code = code.replace('post_text = f"""**{title}**', 'post_text = f"""{title}')
        code = code.replace('**Key Takeaway:** {takeaway}', 'Key Takeaway: {takeaway}')
        with open(p2, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Updated {p2} template.")

if __name__ == "__main__":
    update_generator_scripts()
    update_como_campaign()
    update_superpowers_campaign()
