#Weather app

import requests

print("============== WELCOME TO WEATHER SIMULATOR ==============")

def weather(latitude, longitude):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

    response = requests.get(url)
    data = response.json()

    temperature = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    wind_speed = data["current"]["wind_speed_10m"]

    return temperature, humidity, wind_speed


while True:

    print("\n1. Check weather of your current location")
    print("2. Search weather by city")
    print("3. Exit")

    x = input("Enter your choice: ")

    if x == "1":

        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        location = data["city"]
        latitude, longitude = data["loc"].split(",")

        temperature, humidity, wind_speed = weather(latitude, longitude)

        print(f"\nLocation: {location}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

    elif x == "2":

        city = input("Enter the city: ")

        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

        response = requests.get(geo_url)
        data_geo = response.json()

        if "results" not in data_geo:
            print("City not found")
            continue

        location = data_geo["results"][0]["name"]
        latitude = data_geo["results"][0]["latitude"]
        longitude = data_geo["results"][0]["longitude"]

        temperature, humidity, wind_speed = weather(latitude, longitude)

        print(f"\nLocation: {location}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

    elif x == "3":
        print("Thank you for using Weather Simulator!")
        break

    else:
        print("Invalid option. Please try again.")