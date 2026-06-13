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
    lines = []
    cur = ""
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


def terminal_slide(path, title, lines, accent="#38bdf8"):
    img = Image.new("RGB", (1280, 720), "#0b1020")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1280, 52], fill="#111827")
    d.ellipse([24, 18, 38, 32], fill="#ef4444")
    d.ellipse([48, 18, 62, 32], fill="#f59e0b")
    d.ellipse([72, 18, 86, 32], fill="#22c55e")
    d.text((108, 15), title, font=font(22, True), fill="#e5e7eb")
    d.rectangle([56, 86, 1224, 644], fill="#050816", outline=accent, width=2)
    y = 116
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
        for part in wrap(d, line, font(22), 1080):
            d.text((84, y), part, font=font(22), fill=color)
            y += 32
        y += 4
    img.save(path)


def plain_slide(path, title, body, accent="#38bdf8"):
    img = Image.new("RGB", (1280, 720), "#0b1020")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1280, 12], fill=accent)
    d.text((72, 72), title, font=font(52, True), fill="#f8fafc")
    y = 180
    for line in body:
        for part in wrap(d, line, font(30), 1080):
            d.text((88, y), part, font=font(30), fill="#dbeafe")
            y += 46
        y += 14
    d.text((72, 650), "InvariantLab · DeFi invariant verification", font=font(22), fill="#94a3b8")
    img.save(path)


def main():
    sample = subprocess.run(
        ["python3", "scripts/invariantlab_demo.py", "--sample"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.strip().splitlines()

    plain_slide(
        DEMO / "demo-01.png",
        "InvariantLab",
        [
            "AI-assisted DeFi invariant verification.",
            "The tool turns a security hypothesis into runnable evidence: invariant, PoC result, measured impact, and patch direction.",
        ],
    )
    terminal_slide(
        DEMO / "demo-02.png",
        "Terminal demo",
        ["$ python3 scripts/invariantlab_demo.py --sample"] + sample,
        "#22c55e",
    )
    plain_slide(
        DEMO / "demo-03.png",
        "What the result means",
        [
            "The demo checks a vault launch invariant: a new vault should not accept the first external share before setup and activation.",
            "The output reports test pass count, protocol NAV, attacker profit excluding the 1 wei principal, stuck cached assets, and a patch recommendation.",
        ],
        "#a78bfa",
    )
    plain_slide(
        DEMO / "demo-04.png",
        "Agent safety layer",
        [
            "Before an AI agent moves capital on-chain, InvariantLab can check protocol-specific economic invariants.",
            "Next step: connect this runner to mainnet-fork replay and MCP tools for agent workflows.",
        ],
        "#f59e0b",
    )

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-framerate",
            "1/6",
            "-i",
            "demo/demo-%02d.png",
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
