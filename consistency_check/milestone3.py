#!/usr/bin/env python3
from utils import Utilities
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json, random, decimal

# number of tests
N = 20
# Distance threshold 50 m
D = 0.05

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
	plt.plot(i[0],i[1],'m*')

plt.ion()
plt.grid()
red_patch = mpatches.Patch(color='red', label='Original')
blue_patch = mpatches.Patch(color='blue', label='Extended')
plt.legend(handles=[red_patch, blue_patch])
plt.title('Original Path VS Extended ')
plt.draw()
plt.gca().set_aspect('equal', adjustable='box')

for i in range(N):
    # Define random control point C and plot it. Hardcoding random ranges
    x_c = float(decimal.Decimal(random.randrange(0,50))/100)
    y_c = float(decimal.Decimal(random.randrange(0,50))/100)
    C = ( x_c , y_c )

    pt_star,dist = utils.find_closest_point_in_path(C,projected_coord_extended)

    if dist <= D:
        color_pt = 'go'
        color_check = 'g*'
    else:
        color_pt = 'ro'
        color_check = 'r*'

    plt.plot( x_c, y_c, color_check, markersize=12)
    plt.plot( pt_star[0], pt_star[1] , color_pt, markersize=12)
    plt.pause(0.5)

input("Press [enter] to continue.")
