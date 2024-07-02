import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

def get_weather():
    city_name = city_entry.get()
    api_key = "b22528876c1a7ba8206f9fc1677c094e"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        city_label.config(text=city_name)
        temp_label.config(text=f"{main['temp']}°C")
        desc_label.config(text=weather['description'].capitalize())
        feels_like_label.config(text=f"Feels like {main['feels_like']}°C")
        wind_label.config(text=f"Wind: {wind['speed']} m/s")
        humidity_label.config(text=f"Humidity: {main['humidity']}%")
        pressure_label.config(text=f"Pressure: {main['pressure']} hPa")
        current_time_label.config(text=datetime.now().strftime("%I:%M %p"))
    else:
        messagebox.showerror("Error", "City not found or API request failed.")

# Set up the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

# Background
background_image = Image.open("D:/Arcade Work/image_weather.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(app, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# City Entry
city_entry = tk.Entry(app, font=("Helvetica", 16), bd=0, relief="flat", justify="center")
city_entry.place(x=110, y=25, width=180, height=30)

# Search Button
search_button = tk.Button(app, text="Search", font=("Helvetica", 12), command=get_weather)
search_button.place(x=300, y=25, width=70, height=30)

# City Name Label
city_label = tk.Label(app, text="", font=("Helvetica", 20, "bold"), bg="white")
city_label.place(x=20, y=80)

# Current Time Label
current_time_label = tk.Label(app, text="", font=("Helvetica", 12), bg="white")
current_time_label.place(x=20, y=120)

# Temperature Label
temp_label = tk.Label(app, text="", font=("Helvetica", 44), bg="white")
temp_label.place(x=150, y=100)

# Description Label
desc_label = tk.Label(app, text="", font=("Helvetica", 12), bg="white")
desc_label.place(x=150, y=160)

# Feels Like Label
feels_like_label = tk.Label(app, text="", font=("Helvetica", 12), bg="white")
feels_like_label.place(x=150, y=180)

# Wind Label
wind_label = tk.Label(app, text="", font=("Helvetica", 12), bg="white")
wind_label.place(x=20, y=220)

# Humidity Label
humidity_label = tk.Label(app, text="", font=("Helvetica", 12), bg="white")
humidity_label.place(x=120, y=220)

# Pressure Label
pressure_label = tk.Label(app, text="", font=("Helvetica", 12), bg="white")
pressure_label.place(x=220, y=220)

# Run the main event loop
app.mainloop()
