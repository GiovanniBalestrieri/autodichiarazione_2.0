import openrouteservice
from openrouteservice import convert

token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'


coords = ((8.34234,48.23424),(8.34423,48.26424))

client = openrouteservice.Client(key=token) # Specify your personal API key
#routes = client.directions(coords)

# decode_polyline needs the geometry only
geometry = client.directions(coords)['routes'][0]['geometry']

decoded = convert.decode_polyline(geometry)

print(decoded)

