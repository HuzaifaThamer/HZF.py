# 💻 HZF.py
# 🐍 PROJECT 09/30

from PIL import Image
from pathlib import Path
import os

folder = Path("images")
output = Path("images.pdf")

files = sorted(
    list(folder.glob("*.jpg"))
    + list(folder.glob("*.png"))
    + list(folder.glob("*.jpeg"))
    )

images = [
    Image.open(file).convert("RGB")
    for file in files
]

images[0].save(
    output,
    optimize=True,
    append_images=images[1:],
)

os.startfile(output.resolve())