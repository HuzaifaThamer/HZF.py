import yt_dlp

url = input("Enter the url you want to download: ")

options = {
    "format": "bestaudio/best",
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])