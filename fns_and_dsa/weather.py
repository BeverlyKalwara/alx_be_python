import requests

# Replace with your own WeatherAPI key
API_KEY = "90945be98ea945fcbd9200152251510"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

# Ask user for city name
city = input("Enter a city name to check its weather: ")

# Build full API request URL
url = f"{BASE_URL}?key={API_KEY}&q={city}"

# Make the GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dictionary

    # Extract useful weather information
    location = data['location']['name']
    country = data['location']['country']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']

    # Display weather info
    print(f"\nWeather in {location}, {country}:")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")

else:
    print("Error fetching weather data. Please check your city name or API key.")