#!/usr/bin/env python3
from utils import Utilities
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json

# Load sequence of gps positions
with open('path.json') as f:
  data = json.load(f)

# Set reference point for the projection. It will be our origin of our reference system
utils = Utilities(data[0])

# Store new projected points
projected_coord = []
projected_coord_extended = []

# Project coordinates
for idx,i in enumerate(data):
	if idx == 0:
		projected_coord.append(utils.project(i))
		continue
	# Store a projected version of our gps coordinates
	projected_coord.append(utils.project(i))
	
	# Store the new extended path 
	projected_coord_extended.extend(utils.explode_segment(utils.project(data[idx-1]), utils.project(i)))

# Plot extended path
for i in projected_coord_extended: 
	plt.plot(i[0],i[1],'bo')

# Plot projected original path in red
for i in projected_coord: 
	plt.plot(i[0],i[1],'r*')

plt.grid()
red_patch = mpatches.Patch(color='red', label='Original')
blue_patch = mpatches.Patch(color='blue', label='Extended')
plt.legend(handles=[red_patch, blue_patch])
plt.title('Original Path VS Extended ')
plt.show()
