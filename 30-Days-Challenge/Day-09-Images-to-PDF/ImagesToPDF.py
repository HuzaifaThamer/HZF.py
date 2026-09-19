# 💻 HZF.py
# 🐍 PROJECT 10 / 30

from pathlib import Path
import hashlib

folder = Path("files")
seen = {}
duplicates = []

for file in folder.rglob("*"):
    if not file.is_file():
        continue

        with file.open("rb") as f:
            file_hash = hashlib.file_digest(f, "sha256").hexdigest()

        if file_hash in seen:
            duplicates.append((file, seen[file_hash]))

        else:
            seen[file_hash] = file

    for duplicate, original in duplicates:
        print(f"{duplicate.name} -> {original.name}")

    print(f"\n{len(duplicates)} duplicates files found")





















