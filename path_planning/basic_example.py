import openrouteservice
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'


coords = ((8.34234,48.23424),(8.34423,48.26424))

client = openrouteservice.Client(key=token) # Specify your personal API key
routes = client.directions(coords)

print(routes)
print("\n\nAAAA\n\n")
print(routes['routes'][0]['geometry'])

