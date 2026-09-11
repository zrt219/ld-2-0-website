import os
import shutil

src_dir = r"C:\Users\Zhane\Documents\Website stuff\lornetteig\Career Circle Posts\SEPTEMBER linkined ads\como win"
dst_dir = r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\public\campaigns\como-win"

os.makedirs(dst_dir, exist_ok=True)

file_map = {
    "-SEkh-Te06plQAqJ.mp4": "como-vid-01-anthem.mp4",
    "bhmA6_iYfJq3F4Kd.mp4": "como-vid-02-goal.mp4",
    "CyWE4AJP8sNNeCeQ.mp4": "como-vid-03-cesc-celebration.mp4",
    "yzBpFojKgwkKuPBe.mp4": "como-vid-04-cbs-interview.mp4",
    "ChatGPT Image Sep 10, 2026, 08_25_56 PM (1).png": "como-img-01-fulltime.png",
    "ChatGPT Image Sep 10, 2026, 08_25_56 PM (2).png": "como-img-02-in-europa.png",
    "ChatGPT Image Sep 10, 2026, 08_25_58 PM (3).png": "como-img-03-match-report.png",
    "ChatGPT Image Sep 10, 2026, 08_25_58 PM (4).png": "como-img-04-assane-diao.png",
    "ChatGPT Image Sep 10, 2026, 08_25_59 PM (5).png": "como-img-05-maximo-perrone.png",
    "ChatGPT Image Sep 10, 2026, 08_25_59 PM (6).png": "como-img-06-sinigaglia-night.png",
    "ChatGPT Image Sep 10, 2026, 08_25_59 PM (7).png": "como-img-07-one-club.png",
    "ChatGPT Image Sep 10, 2026, 08_25_59 PM (8).png": "como-img-08-lariani-flag.png"
}

for src_name, dst_name in file_map.items():
    s = os.path.join(src_dir, src_name)
    d = os.path.join(dst_dir, dst_name)
    if os.path.exists(s):
        shutil.copy2(s, d)
        size = os.path.getsize(d)
        print(f"Copied {src_name} -> {dst_name} ({size:,} bytes)")
    else:
        print(f"WARNING: Missing source file: {s}")

print("\nStaged files in destination:")
for f in sorted(os.listdir(dst_dir)):
    sz = os.path.getsize(os.path.join(dst_dir, f))
    print(f"  {f}: {sz:,} bytes")
