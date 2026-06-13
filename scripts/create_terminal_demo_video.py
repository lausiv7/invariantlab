#!/usr/bin/env python3
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo"
DEMO.mkdir(exist_ok=True)


def font(size, bold=False):
    name = "DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        test = f"{cur} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def terminal_frame(path):
    output = subprocess.run(
        ["python3", "scripts/invariantlab_demo.py", "--sample"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.strip().splitlines()

    lines = ["$ python3 scripts/invariantlab_demo.py --sample"] + output
    img = Image.new("RGB", (1280, 720), "#050816")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1280, 52], fill="#111827")
    d.ellipse([24, 18, 38, 32], fill="#ef4444")
    d.ellipse([48, 18, 62, 32], fill="#f59e0b")
    d.ellipse([72, 18, 86, 32], fill="#22c55e")
    d.text((108, 15), "terminal", font=font(22, True), fill="#e5e7eb")

    y = 88
    for line in lines:
        color = "#dbeafe"
        if line.startswith("$"):
            color = "#7dd3fc"
        elif "5 passed" in line:
            color = "#86efac"
        elif "attacker_profit" in line or "stuck_cached" in line:
            color = "#fde68a"
        elif "patch_recommendation" in line:
            color = "#c4b5fd"
        for part in wrap(d, line, font(24), 1130):
            d.text((68, y), part, font=font(24), fill=color)
            y += 36
        y += 4
    img.save(path)


def main():
    frame = DEMO / "terminal-demo.png"
    terminal_frame(frame)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(frame),
            "-t",
            "18",
            "-vf",
            "format=yuv420p",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "demo/invariantlab-demo.mp4",
        ],
        cwd=ROOT,
        check=True,
    )
    print(ROOT / "demo/invariantlab-demo.mp4")


if __name__ == "__main__":
    main()
