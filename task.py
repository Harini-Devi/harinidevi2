import requests
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found or an error occurred.")
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "4a54ce47cb6bdf53d3db965a905b2b06"
    get_weather(city_name, api_key)
