import urllib.request
import urllib.parse
import json

place = "Kraków"
encoded_place = urllib.parse.quote(place)
url = f"https://nominatim.openstreetmap.org/search?q={encoded_place}&format=json"

headers = {"User-Agent": "Python App"}

request = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(request) as response:
    data = response.read()

data = json.loads(data.decode('utf-8'))
if data:
    latitude = data[0]['lat']
    longitude = data[0]['lon']
    print(f"Szerokość: {latitude}, Długość: {longitude}")
else:
    print("Nie znaleziono wyników dla podanego miejsca.")
