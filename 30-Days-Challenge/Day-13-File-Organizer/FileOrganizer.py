from pathlib import Path
import shutil

folder = Path("files")

categories = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

for file in folder.iterdir():
    if file.is_file():
        for category, extensions in categories.items():
            if file.suffix.lower() in extensions:

                destination = folder / category
                destination.mkdir(exist_ok= True)

                shutil.move(file, destination / file.name)

                break






















