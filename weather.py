import os
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import pytz
import requests
from dotenv import load_dotenv
from geopy.exc import GeopyError
from geopy.geocoders import Nominatim

# from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder

# Build main window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# API connect
load_dotenv()
api_key = os.getenv("API_key")

# Folder that holds all the app images
IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")


def image_path(filename):
    return os.path.join(IMAGE_DIR, filename)


def getWeather():
    city = textField.get().strip()
    if not city:
        messagebox.showwarning("Weather App", "Please enter a location.")
        return

    try:
        geoLocator = Nominatim(user_agent="weather-app-api")
        location = geoLocator.geocode(city, timeout=10)
    except GeopyError as e:
        messagebox.showerror("Weather App", f"Location service error:\n{e}")
        return

    if location is None:
        messagebox.showerror("Weather App", f"Location '{city}' not found.")
        return

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    clock.config(text=current_time)
    name.config(text="Current weather at")

    # Weather details
    if not api_key:
        messagebox.showerror("Weather App", "API_key is missing.")
        return

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": location.latitude,
                "lon": location.longitude,
                "appid": api_key,
                "units": "metric",  # temperatures in °C, wind in m/s
            },
            timeout=10,
        )
        json_data = response.json()

    except (requests.RequestException, ValueError) as e:
        messagebox.showerror("Weather App", f"Could not reach weather service:\n{e}")
        return

    # On failure OpenWeather returns e.g. {"cod": 401, "message": "Invalid API key..."}
    if response.status_code != 200:
        messagebox.showerror(
            "Weather App",
            f"Weather API error: {json_data.get('message', response.text)}",
        )
        return

    condition = json_data["weather"][0]["main"]
    description = json_data["weather"][0]["description"]
    temp = round(json_data["main"]["temp"])
    feels_like = round(json_data["main"]["feels_like"])
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]

    temperature.config(text=f"{temp}°")
    conditions.config(text=f"{condition} | FEELS LIKE {feels_like}°")
    wind_value.config(text=f"{wind} m/s")
    humidity_value.config(text=f"{humidity}%")
    description_value.config(text=description)
    pressure_value.config(text=f"{pressure} hPa")


# Search box
Search_image = PhotoImage(file=image_path("search.png"))

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

search_icon = PhotoImage(file=image_path("search_icon.png"))
search_box_btn = Button(
    image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather
)
search_box_btn.place(x=400, y=34)

# Logo
log_image = PhotoImage(file=image_path("logo.png"))
logo = Label(image=log_image)
logo.place(x=150, y=100)

# Bottom box
frame_image = PhotoImage(file=image_path("box.png"))
frame_box = Label(image=frame_image)
frame_box.pack(padx=5, pady=5, side="bottom")

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)

clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

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
label_DESCRIPTION.place(x=400, y=400)

label_PRESSURE = Label(
    root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1AB5EF"
)
label_PRESSURE.place(x=650, y=400)

# Value labels
temperature = Label(font=("arial", 70, "bold"), fg="#ee666d")
temperature.place(x=400, y=150)

conditions = Label(font=("arial", 15, "bold"))
conditions.place(x=400, y=250)

wind_value = Label(text="...", font=("arial", 20), bg="#1AB5EF")
wind_value.place(x=120, y=430)

humidity_value = Label(text="...", font=("arial", 20), bg="#1AB5EF")
humidity_value.place(x=280, y=430)

description_value = Label(text="...", font=("arial", 20), bg="#1AB5EF")
description_value.place(x=400, y=430)

pressure_value = Label(text="...", font=("arial", 20), bg="#1AB5EF")
pressure_value.place(x=650, y=430)
root.mainloop()
