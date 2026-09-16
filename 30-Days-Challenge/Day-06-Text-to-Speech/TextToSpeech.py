# 💻 HZF.py
# 🐍 PROJECT 06 / 30
from tkinter.constants import CENTER

from gtts import gTTS
import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x500")
app.title("Text to Voice")

def generate():
    text= text_input.get()
    voice= gTTS(text=text, lang='en', slow=False)
    voice.save("test.mp3")



generate_button = ctk.CTkButton(app,
                                text="Generate",
                                fg_color="red",
                                command=generate)
generate_button.place(relx=0.5,rely=0.48,anchor="center")

text_input= ctk.CTkEntry(app,
                         width=200)
text_input.place(relx=0.5,rely=0.4,anchor="center")


app.mainloop()













