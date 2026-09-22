import importlib.util
import os
import re

campaign_scripts = [
    ("vintage-nfl", "schedule-vintage-nfl-campaign.py", 24),
    ("macclung", "schedule-macclung-campaign.py", 11),
    ("jazzy-davidson", "schedule-jazzy-davidson-campaign.py", 10),
    ("mendoza", "schedule-mendoza-campaign.py", 20),
    ("nba", "schedule-nba-campaign.py", 3),
    ("cricket", "schedule-cricket-campaign.py", 14),
    ("sitaya-fagan", "schedule-sitaya-fagan-campaign.py", 10),
    ("tyrese-gibson", "schedule-tyrese-gibson-campaign.py", 12),
    ("yaroslava-mahuchikh", "schedule-yaroslava-mahuchikh-campaign.py", 8),
    ("saquon-barkley", "schedule-saquon-barkley-campaign.py", 10)
]

scripts_dir = "scripts"
all_errors = []

for camp, sname, expected_count in campaign_scripts:
    spath = os.path.join(scripts_dir, sname)
    if not os.path.exists(spath):
        all_errors.append(f"MISSING: {spath}")
        continue
    
    with open(spath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for em dash
    if "\u2014" in content or "—" in content or "&mdash;" in content:
        all_errors.append(f"EM DASH in {sname}")

    # Import and check posts_data
    try:
        spec = importlib.util.spec_from_file_location(camp.replace('-', '_'), spath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        posts = getattr(mod, "posts_data", [])
        if len(posts) != expected_count:
            all_errors.append(f"COUNT MISMATCH in {sname}: found {len(posts)}, expected {expected_count}")
        
        for p in posts:
            p_id = p.get("id")
            text = p.get("text", "")
            if "\u2014" in text or "—" in text:
                all_errors.append(f"EM DASH in {sname} post #{p_id}")
            
            url = p.get("assetUrl", "")
            if not url.startswith(f"https://lornettedaye.com/campaigns/{camp}/"):
                all_errors.append(f"INVALID URL in {sname} post #{p_id}: {url}")
                
            dueAt = p.get("dueAt", "")
            if not dueAt or not dueAt.endswith("Z"):
                all_errors.append(f"INVALID dueAt in {sname} post #{p_id}: {dueAt}")

    except Exception as e:
        all_errors.append(f"IMPORT ERROR in {sname}: {e}")

print("=== AUDIT SUMMARY ===")
if all_errors:
    print(f"Found {len(all_errors)} errors:")
    for err in all_errors:
        print("  -", err)
else:
    print("ALL 10 SCRIPTS PASSED DATA AND SYNTAX AUDIT!")
