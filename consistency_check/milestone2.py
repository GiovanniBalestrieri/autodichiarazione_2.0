#!/usr/bin/env python3
from utils import Utilities
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json, random, decimal

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
plt.ion()
red_patch = mpatches.Patch(color='red', label='Original')
blue_patch = mpatches.Patch(color='blue', label='Extended')
plt.legend(handles=[red_patch, blue_patch])
plt.title('Original Path VS Extended ')
plt.draw()
plt.gca().set_aspect('equal', adjustable='box')
plt.pause(0.001)

# Define random control point C and plot it. Hardcoding random ranges
x_c = float(decimal.Decimal(random.randrange(0,50))/100)
y_c = float(decimal.Decimal(random.randrange(0,50))/100)
C = ( x_c , y_c )
plt.plot(x_c,y_c,'k*')

# Find closest point to C in the discretized path and plot it
index = utils.closest_node((x_c,y_c),projected_coord_extended)
Pp = (projected_coord_extended[index][0] , projected_coord_extended[index][1] )
#plt.plot(Pp[0], Pp[1] ,'c*')

# Once we have the closest point Pp of the discretized path,
# We need to consider two possible segments and find the closest point to C

# Consider three cases:
if index == 0 and index+1 < len(projected_coord_extended):
    Pp_next = (projected_coord_extended[index+1][0] , projected_coord_extended[index+1][1] )
    candidate1, dist1 = utils.closest_point_to_segment(Pp[0],Pp[1],Pp_next[0], Pp_next[1], C )
    pt_star = candidate1
elif index == len(projected_coord_extended)-1:
    Pp_prev = (projected_coord_extended[index-1][0] , projected_coord_extended[index-1][1] )
    candidate2, dist2 = utils.closest_point_to_segment(Pp[0],Pp[1],Pp_prev[0], Pp_prev[1] , C)
    pt_star = candidate2
else:
    Pp_next = (projected_coord_extended[index+1][0] , projected_coord_extended[index+1][1] )
    candidate1, dist1 = utils.closest_point_to_segment(Pp[0],Pp[1],Pp_next[0], Pp_next[1], C )
    Pp_prev = (projected_coord_extended[index-1][0] , projected_coord_extended[index-1][1] )
    candidate2, dist2 = utils.closest_point_to_segment(Pp[0],Pp[1],Pp_prev[0], Pp_prev[1] , C)
    # Pick the closest one
    pt_star = candidate1 if dist1 <= dist2  else candidate2

plt.plot( pt_star[0], pt_star[1] ,'c*')

input("Press [enter] to continue.")
