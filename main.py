import requests
import csv
import os

def get_location(Location):
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    location_info = {
    "name": Location
    }

    try:
        r1 = requests.get(geocoding_url, params=location_info, timeout=10)
        r1.raise_for_status()
        value = r1.json()

    except requests.exceptions.Timeout as g:
        print(f"Request timed out: {g}")
        exit()

    except requests.exceptions.ConnectionError as f:
        print(f"Connection error occurred: {f}")
        exit()

    except requests.exceptions.HTTPError as h:
        print(f"HTTP error occurred: {h}")
        exit()    

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching location data: {e}")
        exit()

    except requests.exceptions.JSONDecodeError as j:
        print(f"Error decoding JSON response: {j}")
        exit()

    if not value.get("results"):
        print("Location not found. Please check the spelling or try a different location.")
        exit()


    latitude = value["results"][0]["latitude"]
    longitude = value["results"][0]["longitude"]

    return latitude, longitude

    
def get_weather(latitude, longitude):
    forecast_url = "https://api.open-meteo.com/v1/forecast"

    weather_info={
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        r2 = requests.get(forecast_url, params=weather_info, timeout=10)
        r2.raise_for_status()
        data = r2.json()
        
    except requests.exceptions.Timeout as g:
        print(f"Request timed out: {g}")
        exit()

    except requests.exceptions.ConnectionError as f:
        print(f"Connection error occurred: {f}")
        exit()

    except requests.exceptions.HTTPError as h:
        print(f"HTTP error occurred: {h}")
        exit()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")
        exit()
    except requests.exceptions.JSONDecodeError as j:
        print(f"Error decoding JSON response: {j}")
        exit()

    Temperature = data["current"]["temperature_2m"]
    Humidity = data["current"]["relative_humidity_2m"]
    Wind_Speed = data["current"]["wind_speed_10m"]

    print(f"Temperature: {Temperature}°C")
    print(f"Humidity: {Humidity}%")
    print(f"Wind Speed: {Wind_Speed} km/h")

    return Temperature, Humidity, Wind_Speed


def save_to_csv(Location, Temperature, Humidity, Wind_Speed):

    if not os.path.exists("weather_data.csv"):
        with open("weather_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Location", "Temperature", "Humidity", "Wind Speed"])
            writer.writerow([Location, Temperature, Humidity, Wind_Speed])
            

    else:
        with open("weather_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([Location, Temperature, Humidity, Wind_Speed])

    return True



def main():
    print("Weather Data Collector started!")
    
    Location = input("Enter the location for which you want to get the weather data (e.g., city name): ")

    latitude, longitude = get_location(Location)
    Temperature, Humidity, Wind_Speed = get_weather(latitude, longitude)
    save_to_csv(Location, Temperature, Humidity, Wind_Speed)   

    return True

main()