"""Compress the two generated photos and emit inline base64 data URIs.

Outputs:
  assets/inline_hero.b64   -> data:image/jpeg;base64,...  (city aerial, Hero)
  assets/inline_crowd.b64  -> data:image/jpeg;base64,...  (diverse crowd, regional section)
No external links are used in the final page; images are embedded as data URIs.
"""
import base64
import io
from pathlib import Path

from PIL import Image

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SRC = {
    "hero": ASSETS / "A_dramatic_high_angle_aerial_p_2026-08-16T02-39-01.png",
    "crowd": ASSETS / "A_diverse__colorful_crowd_of_p_2026-08-16T02-39-01.png",
}
MAX_W = 1280
QUALITY = 82


def to_data_uri(path: Path) -> str:
    img = Image.open(path).convert("RGB")
    if img.width > MAX_W:
        h = round(img.height * MAX_W / img.width)
        img = img.resize((MAX_W, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


for key, src in SRC.items():
    uri = to_data_uri(src)
    out = ASSETS / f"inline_{key}.b64"
    out.write_text(uri, encoding="utf-8")
    kb = len(uri) / 1024
    print(f"{key}: {out.name}  ({kb:.0f} KB data uri, source {src.name})")
