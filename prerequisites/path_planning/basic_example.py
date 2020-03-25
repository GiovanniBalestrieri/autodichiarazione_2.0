import openrouteservice
from openrouteservice import convert

# Change your token here
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'

# Setting POIs
home =  (5.710752, 45.178611) 
market_1 = (5.709025, 45.175798)
work_spot = (5.807179, 45.216604)
 
# Create coordinates tuple
market_one_way = (home,market_1)
market_round_trip = (home, market_1, home)
work_round_trip = (home, work_spot, home)

# Connect to client
client = openrouteservice.Client(key=token) # Specify your token

# decode_polyline needs the geometry only
geometry = client.directions(market_one_way)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

print(decoded['coordinates'])

