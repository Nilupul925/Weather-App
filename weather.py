import tkinter as tk
from tkinter import *

from geopy.geocoders import Nominatim

# from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder

# from datetime import datetime
# import requests
# import pytz

# Build main window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getWeather():
    city = textField.get()

    geoLocator = Nominatim(user_agent="weather-app-api")
    location = geoLocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    # To check the result
    print(result)


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
search_box_btn = Button(
    image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather
)
search_box_btn.place(x=400, y=34)

# Logo
log_image = PhotoImage(file="logo.png")
logo = Label(image=log_image)
logo.place(x=150, y=100)

# Bottom box
frame_image = PhotoImage(file="box.png")
frame_box = Label(image=frame_image)
frame_box.pack(padx=5, pady=5, side="bottom")

# Bottom box columns
label_WIND = Label(
    root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF"
)
label_WIND.place(x=120, y=400)

label_HUMIDITY = Label(
    root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF"
)
label_HUMIDITY.place(x=250, y=400)

label_DESCRIPTION = Label(
    root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF"
)
label_DESCRIPTION.place(x=430, y=400)

label_PRESSURE = Label(
    root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF"
)
label_PRESSURE.place(x=650, y=400)

# Value labels
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

wind_value = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
wind_value.place(x=120, y=430)

humidity_value = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
humidity_value.place(x=250, y=430)

description_value = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
description_value.place(x=430, y=430)

pressure_value = Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
pressure_value.place(x=650, y=430)
root.mainloop()
