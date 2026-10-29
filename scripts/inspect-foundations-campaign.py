import os
import glob
import csv

root_dir = r"C:\Users\Zhane\Documents\Website stuff\lornetteig\FOUNDATIONS"
cartoon_dir = os.path.join(root_dir, "cartoon")
csv_path = os.path.join(cartoon_dir, "linkedin_lornette_umattr_90_day_schedule.csv")

root_pngs = {os.path.basename(p): p for p in glob.glob(os.path.join(root_dir, "*.png"))}
cartoon_pngs = {os.path.basename(p): p for p in glob.glob(os.path.join(cartoon_dir, "*.png"))}

print("Root PNGs:", len(root_pngs))
print("Cartoon PNGs:", len(cartoon_pngs))

all_local = {}
for k, v in root_pngs.items():
    all_local[k.lower()] = v
for k, v in cartoon_pngs.items():
    all_local[k.lower()] = v

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("Total CSV rows:", len(rows))
csv_images = sorted(list(set(r["Image_File"] for r in rows)))
print("Unique images in CSV:", len(csv_images))

missing = []
found = []
for img in csv_images:
    clean_name = img.lower().strip()
    match = all_local.get(clean_name)
    if not match:
        # try replacing spaces with underscores or vice versa
        for lk, lv in all_local.items():
            if clean_name.replace("-", "_").replace(" ", "_") == lk.replace("-", "_").replace(" ", "_"):
                match = lv
                break
            if clean_name.split(".")[0] in lk:
                match = lv
                break
    if match:
        found.append((img, match))
        print("  MATCH:", img, "->", os.path.basename(match))
    else:
        missing.append(img)
        print("  MISSING:", img)

print("Found:", len(found), "Missing:", len(missing))
