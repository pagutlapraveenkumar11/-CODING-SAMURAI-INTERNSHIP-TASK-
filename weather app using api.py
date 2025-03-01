import requests

api_key = '4f6a2d64296ddaffd743d452f5785cc5'

user_input = input('Enter the city name: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)

# Convert response to JSON
data = weather_data.json()

# Check if city is found
if data['cod'] == 404:
    print("No City Found")
else:
    weather = data['weather'][0]['main']  # Fix key case
    temp = round(data['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
