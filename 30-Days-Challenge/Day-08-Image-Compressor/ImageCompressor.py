from PIL import Image
from pathlib import Path

input_file = Path("photo.jpg")
compressed_file = Path("compressed.jpg")

image = Image.open(input_file).convert("RGB")

image.save(compressed_file, "JPEG", quality=70, optimize=True)