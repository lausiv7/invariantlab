#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DEMO = ROOT / "demo"
ASSETS.mkdir(exist_ok=True)
DEMO.mkdir(exist_ok=True)


def font(size, bold=False):
    name = "DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    return ImageFont.truetype(str(path), size)


def centered(draw, xy, text, fnt, fill):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = xy[0] - (bbox[2] - bbox[0]) / 2
    y = xy[1] - (bbox[3] - bbox[1]) / 2
    draw.text((x, y), text, font=fnt, fill=fill)


def logo():
    img = Image.new("RGB", (480, 480), "#0b1020")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([40, 40, 440, 440], radius=64, fill="#111827", outline="#38bdf8", width=4)
    d.line([120, 285, 185, 210, 245, 250, 330, 155, 370, 195], fill="#22c55e", width=12, joint="curve")
    d.ellipse([105, 270, 135, 300], fill="#38bdf8")
    d.ellipse([170, 195, 200, 225], fill="#38bdf8")
    d.ellipse([230, 235, 260, 265], fill="#38bdf8")
    d.ellipse([315, 140, 345, 170], fill="#38bdf8")
    d.ellipse([355, 180, 385, 210], fill="#38bdf8")
    centered(d, (240, 330), "Invariant", font(40, True), "#f8fafc")
    centered(d, (240, 378), "Lab", font(40, True), "#38bdf8")
    img.save(ASSETS / "invariantlab-logo-480.png")


def slide(path, title, body, accent="#38bdf8"):
    img = Image.new("RGB", (1280, 720), "#0b1020")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1280, 12], fill=accent)
    d.text((72, 70), title, font=font(48, True), fill="#f8fafc")
    y = 170
    for line in body:
        d.text((86, y), line, font=font(30), fill="#dbeafe")
        y += 52
    d.text((72, 650), "InvariantLab · AI-assisted DeFi invariant verification", font=font(22), fill="#94a3b8")
    img.save(path)


def slides():
    slide(
        DEMO / "slide-01.png",
        "InvariantLab",
        [
            "AI-assisted DeFi invariant discovery",
            "Foundry-based exploit verification",
            "Output: profit, stuck assets, patch direction",
        ],
    )
    slide(
        DEMO / "slide-02.png",
        "Problem",
        [
            "DeFi bugs are often broken economic invariants.",
            "AI reports are cheap; reproducible evidence is scarce.",
            "Protocols need runnable proof, not generic text.",
        ],
        "#f59e0b",
    )
    slide(
        DEMO / "slide-03.png",
        "Workflow",
        [
            "Target repo -> invariant definition",
            "Foundry PoC runner -> evidence parser",
            "Risk signal -> patch recommendation",
        ],
        "#22c55e",
    )
    slide(
        DEMO / "slide-04.png",
        "Demo Result",
        [
            "tests: 5 passed",
            "attacker_profit_excluding_1_wei: 604462909807314587353087",
            "stuck_cached_total_assets: 604462909807314587353088",
        ],
        "#a78bfa",
    )
    slide(
        DEMO / "slide-05.png",
        "Agent Safety Layer",
        [
            "Before an AI agent moves capital on-chain,",
            "InvariantLab checks vault/share/oracle invariants",
            "and returns execute/block evidence.",
        ],
        "#38bdf8",
    )


if __name__ == "__main__":
    logo()
    slides()
    print(ASSETS / "invariantlab-logo-480.png")
    print(DEMO)
