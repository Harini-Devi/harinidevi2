import tkinter as tk
from tkinter import messagebox
import requests
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = {
            'city': data['name'],
            'country': data['sys']['country'],
            'description': data['weather'][0]['description'].title(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
    except Exception as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    weather = get_weather(api_key, city)
    if weather:
        result = (
            f"Weather in {weather['city']}, {weather['country']}:\n"
            f"Description: {weather['description']}\n"
            f"Temperature: {weather['temperature']}°C\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Wind Speed: {weather['wind_speed']} m/s"
        )
        weather_label.config(text=result)
api_key = "4a54ce47cb6bdf53d3db965a905b2b06"
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)
city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack(pady=5)
get_weather_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=show_weather)
get_weather_btn.pack(pady=10)
weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=10)
root.mainloop()
