import openrouteservice
from openrouteservice import convert
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Change your token here
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'

# Setting POIs
home =  (5.7116, 45.17695) 
market = (5.71523, 45.18045)
market_1 = (5.709025, 45.175798)
work_spot = (5.807179, 45.216604)
 
# Create coordinates tuple
market_one_way = (home,market)
market_round_trip = (home, market_1, home)
work_one_way = (home, work_spot)
work_round_trip = (home, work_spot, home)

# Connect to client
client = openrouteservice.Client(key=token) # Specify your token

# decode_polyline needs the geometry only
geometry = client.directions(market_one_way)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

path = decoded['coordinates']
print(path)

lons, lats = [ point[0] for point in path ],[ point[1] for point in path]

# Bounding Box definition. Area defined by two longitudes and two latitudes that will include all spatial points.
BBox = (min(lons), max(lons), min(lats), max(lats))
print(BBox)

map_overlay = plt.imread('map.png')

fig, ax = plt.subplots()
ax.scatter(lons,lats, zorder=1, alpha= 0.8, c='b', s=12)
ax.set_title('Plotting Spatial Data on Grenoble Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

ax.imshow(map_overlay, zorder=0, extent = BBox, aspect= 'equal')
plt.show()

