import os
import shutil

src_dir = r"C:\Users\Zhane\Documents\Website stuff\lornetteig\Career Circle Posts\SEPTEMBER linkined ads\alex zverev"
dst_dir = r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\public\campaigns\zverev-usopen"

os.makedirs(dst_dir, exist_ok=True)

file_map = {
    "vT3xap5BM_AueN-N.mp4": "zverev-vid-01-championship-point.mp4",
    "wfyxjfVd1SgCLhZj.mp4": "zverev-vid-02-trophy-lift.mp4",
    "ChatGPT Image Sep 13, 2026, 11_23_06 PM (1).png": "zverev-img-01-he-didnt-realize.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (2).png": "zverev-img-02-heartbreak-to-history.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (3).png": "zverev-img-03-greatness-respects.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (4).png": "zverev-img-04-score-that-changed.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (5).png": "zverev-img-05-he-came-back.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (6).png": "zverev-img-06-first-at-last.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (7).png": "zverev-img-07-the-wait-is-over.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (8).png": "zverev-img-08-champion-magazine.png",
    "ChatGPT Image Sep 13, 2026, 11_23_07 PM (9).png": "zverev-img-09-arthur-ashe-belongs.png",
    "ChatGPT Image Sep 13, 2026, 11_23_08 PM (10).png": "zverev-img-10-crown-is-his.png"
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
