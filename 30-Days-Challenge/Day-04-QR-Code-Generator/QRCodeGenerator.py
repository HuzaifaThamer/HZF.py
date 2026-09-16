# 💻 HZF.py
# 🐍 PROJECT 04 / 30

import qrcode

data= "https://www.instagram.com/hzf.py/"

qr= qrcode.make(data)

qr.save("qrcode.png")

print("QR Code Generated")