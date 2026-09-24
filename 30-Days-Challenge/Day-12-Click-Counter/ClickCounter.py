import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x500")
app.title("Click Counter")
counter_value= 0

def click():
    global counter_value
    counter_value = counter_value + 1
    counter_label.configure(text=f"Counter: {counter_value}")

counter_label = ctk.CTkLabel(app, text="Counter: 0", font=("Arial", 24))
counter_label.place(relx=0.5, rely=0.43, anchor="center")

click_me = ctk.CTkButton(app, text="Click Me", command=click)
click_me.place(relx=0.5, rely=0.50, anchor="center")

app.mainloop()