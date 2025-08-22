import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_weather(data):
    """Display weather information in a readable format."""
    if data is None:
        print("No data to display.")
        return
    
    if data.get('cod') != 200:
        print(f"City not found or error: {data.get('message', '')}")
        return

    city = data['name']
    country = data['sys']['country']
    weather_desc = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\nWeather in {city}, {country}:")
    print(f"Description: {weather_desc}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s\n")

def main():
    print("--- PyWeatherCLI ---")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        if not city:
            print("Please enter a valid city name.")
            continue
        
        data = get_weather(city)
        display_weather(data)

if __name__ == '__main__':
    main()
