import json, random, decimal
import openrouteservice
from openrouteservice import convert

# Change your token here
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'

## Simulate one user and associate a random home gps coordinate

# create boundaries for random points
lat_int = [ 5.7053 , 5.7455 ]
lon_int = [ 45.1786, 45.1933 ]

print(int(lat_int[0]*10000))

home_lat = float(random.randrange( int(lat_int[0]*10000) , int(lat_int[1]*10000))/10000)
home_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)

home = ( home_lat, home_lon )

## Simulate random destination point

dest_lat = float(random.randrange(int(lat_int[0]*10000),int(lat_int[1]*10000))/10000)

dest_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)

dest = ( dest_lat, dest_lon )

## Get detailed navigation instructions and fill the Destinations field of the self declaration
trip = ( home, dest )

# Connect to client
client = openrouteservice.Client(key=token) # Specify your token

# decode_polyline needs the geometry only
geometry = client.directions(trip,profile='foot-walking')['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

path = decoded['coordinates']
print(path)

## Simulate a first self declaration from Home to one destination

## Simulate temporary declaration by pushing it to the distributed digital ledger, the Tangle

