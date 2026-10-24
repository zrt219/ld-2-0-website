# -*- coding: utf-8 -*-
import os
import sys
import json
import shutil

src_dir = r"C:\Users\Zhane\Documents\Website stuff\lornetteig\Career Circle Posts\october ads\coco racism"
target_dir = os.path.join("public", "campaigns", "coco-racism")

os.makedirs(target_dir, exist_ok=True)

files = sorted(os.listdir(src_dir))
print(f"Total source files: {len(files)}")

manifest = []
img_idx = 1

for f in files:
    src_path = os.path.join(src_dir, f)
    if os.path.isdir(src_path):
        continue
    
    ext = os.path.splitext(f)[1].lower()
    
    if ext == ".mp4":
        target_name = "coco-racism-video-01.mp4"
    elif ext in [".png", ".jpg", ".jpeg", ".jfif"]:
        target_name = f"coco-racism-{img_idx:02d}.png"
        img_idx += 1
    else:
        target_name = f"coco-asset-{f}"
        
    target_path = os.path.join(target_dir, target_name)
    shutil.copy2(src_path, target_path)
    
    manifest.append({
        "original": f,
        "target": target_name,
        "size": os.path.getsize(target_path)
    })

print(f"Successfully copied {len(manifest)} assets to {target_dir}")
print(f"Images count: {img_idx - 1}")

with open(os.path.join(target_dir, "manifest.json"), "w", encoding="utf-8") as out:
    json.dump(manifest, out, indent=2)

print("Saved manifest.json.")
