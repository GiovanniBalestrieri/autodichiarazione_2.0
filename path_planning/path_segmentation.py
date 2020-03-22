import openrouteservice
from openrouteservice import convert
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

# Change your token here
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'

# Setting POIs
home =  (5.712608, 45.176793) 
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
geometry = client.directions(market_one_way,profile='foot-walking')['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

path = decoded['coordinates']

# Save segmented path to json
with open('path.json', 'w', encoding='utf-8') as f:
    json.dump(path, f, ensure_ascii=False, indent=4)

print(path)

