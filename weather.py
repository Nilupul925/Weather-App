import tkinter as tk
from tkinter import *

# Build main window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Search box
Search_image = PhotoImage(file="search.png")

search_box = Label(image=Search_image)
search_box.place(x=20, y=20)

textField = tk.Entry(
    root,
    justify="center",
    width=17,
    font=("poppins", 25, "bold"),
    bg="#404040",
    border=0,
    fg="white",
)
textField.place(x=100, y=40)
# Direct keyboard input focus to the this text box
textField.focus()

search_icon = PhotoImage(file="search_icon.png")
search_box_btn = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040")
search_box_btn.place(x=400, y=34)

# Logo
log_image = PhotoImage(file="logo.png")
logo = Label(image=log_image)
logo.place(x=150, y=100)

# Bottom box
frame_image = PhotoImage(file="box.png")
frame_box = Label(image=frame_image)
frame_box.pack(padx=5, pady=5, side="bottom")

root.mainloop()
