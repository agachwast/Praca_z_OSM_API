import urllib.request
import urllib.parse
import json


latitude = 50.06465
longitude = 19.94498

url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"


with urllib.request.urlopen(url) as response:
    data = response.read()


data = json.loads(data.decode('utf-8'))


if 'results' in data:
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    
    print(f"Godzina wschodu słońca: {sunrise}")
    print(f"Godzina zachodu słońca: {sunset}")
else:
    print("Nie udało się uzyskać danych o wschodzie i zachodzie słońca.")
