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

root.mainloop()
