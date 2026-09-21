# 💻 HZF.py
# 🐍 Python day 10/30

import time

text = "HZF.py is the best programming channel"
print(text)

start = time.perf_counter()
typed = input("Type here: ")
second = time.perf_counter() - start

wpm = (len(typed) / 5) / (second / 60)
correct = sum(a == b for a, b in zip(typed, text))
accuracy = correct / len(typed) * 100

print(f"\nSpeed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f} %")
print(f"Time taken: {second:.2f} seconds")