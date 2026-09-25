import customtkinter as ctk
import re


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x550")
app.title("Password Strength Checker")
app.resizable(False, False)


def check_password():
    password = password_entry.get()
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character")

    levels = {
        0: ("Very Weak", "#ff3b3b"),
        1: ("Weak", "#ff5c5c"),
        2: ("Fair", "#ff9f43"),
        3: ("Medium", "#ffd43b"),
        4: ("Strong", "#32d583"),
        5: ("Very Strong", "#00e676")
    }

    strength, color = levels[score]

    strength_label.configure(
        text=f"Strength: {strength}",
        text_color=color
    )

    progress_bar.configure(progress_color=color)
    progress_bar.set(score / 5)

    if not password:
        strength_label.configure(
            text="Strength: —",
            text_color="gray"
        )
        progress_bar.set(0)
        suggestions_label.configure(text="")
        return

    if suggestions:
        suggestions_label.configure(
            text="\n".join(f"• {item}" for item in suggestions)
        )
    else:
        suggestions_label.configure(
            text="✓ Your password looks secure!",
            text_color="#00e676"
        )


def toggle_password():
    if show_password.get() == 1:
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")


title = ctk.CTkLabel(
    app,
    text="Password Strength Checker",
    font=("Arial", 27, "bold")
)
title.pack(pady=(55, 8))


subtitle = ctk.CTkLabel(
    app,
    text="Test how secure your password is",
    text_color="gray",
    font=("Arial", 14)
)
subtitle.pack(pady=(0, 35))


password_entry = ctk.CTkEntry(
    app,
    width=330,
    height=45,
    placeholder_text="Enter your password",
    show="*",
    font=("Arial", 15)
)
password_entry.pack()


show_password = ctk.CTkSwitch(
    app,
    text="Show password",
    command=toggle_password
)
show_password.pack(pady=15)


progress_bar = ctk.CTkProgressBar(
    app,
    width=330,
    height=14
)
progress_bar.pack(pady=(15, 12))
progress_bar.set(0)


strength_label = ctk.CTkLabel(
    app,
    text="Strength: —",
    font=("Arial", 20, "bold"),
    text_color="gray"
)
strength_label.pack()


suggestions_label = ctk.CTkLabel(
    app,
    text="",
    justify="left",
    font=("Arial", 14),
    text_color="#b0b0b0"
)
suggestions_label.pack(pady=20)


password_entry.bind(
    "<KeyRelease>",
    lambda event: check_password()
)


app.mainloop()
