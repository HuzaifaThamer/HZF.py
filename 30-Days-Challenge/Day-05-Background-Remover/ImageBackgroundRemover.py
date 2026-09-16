# 💻 HZF.py
# 🐍 PROJECT 05 / 30

from rembg import remove
from PIL import Image

input_image= Image.open(r"C:\Users\Huzaifa-PC\Desktop\All Python Project V2\YoutubeDownloader\Me.png")
output_image = remove(input_image)
output_image.save("me_logo.png")

print("Image saved")