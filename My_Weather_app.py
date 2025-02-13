import requests

API_KEY = "1f271589d9f804b7120b24c6b4cf89e4"  # Your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  # Example API URL

def get_city_info(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        
        print(f"City: {city}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather}")
    else:
        print("City not found or API request failed!")

# Take user input for city name
city_name = input("Enter a city name: ")
get_city_info(city_name)
