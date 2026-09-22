# 💻 HZF.py
# 🐍 PROJECT 11/30
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x400")
app.title("Login")

email = ctk.CTkEntry(
    app, width=200, placeholder_text="Enter your email"
)
email.place(relx=0.5, rely=0.42, anchor="center")

sign_in = ctk.CTkButton(app, text="Sign in")
sign_in.place(relx=0.5, rely=0.52, anchor="center")

app.mainloop()

















