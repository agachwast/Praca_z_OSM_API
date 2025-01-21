import urllib.request
import urllib.parse
import json
from geopy import Nominatim


def get_coordinates(place):
    geolocator = Nominatim(user_agent="sunrise_app")
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


def get_sun_times(latitude, longitude):
    url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"

    with urllib.request.urlopen(url) as response:
        data = response.read()

    data = json.loads(data.decode('utf-8'))
    if 'results' in data:
        return data['results']['sunrise'], data['results']['sunset']
    else:
        return None, None



def main():
    place = input("Podaj nazwę miejsca (np. Kraków): ")


    latitude, longitude = get_coordinates(place)

    if latitude and longitude:

        sunrise, sunset = get_sun_times(latitude, longitude)

        if sunrise and sunset:
            print(f"Godzina wschodu słońca: {sunrise}")
            print(f"Godzina zachodu słońca: {sunset}")
        else:
            print("Nie udało się pobrać danych o wschodzie i zachodzie słońca.")
    else:
        print("Nie znaleziono współrzędnych dla tego miejsca.")



if __name__ == "__main__":
    main()
