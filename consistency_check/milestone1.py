#!/usr/bin/env python3
from utils import Utilities
import matplotlib.pyplot as plt
import json

# Load sequence of gps positions
with open('path.json') as f:
  data = json.load(f)

utils = Utilities(data[0])


projected_coord = []
projected_coord_extended = []

# Project coordinatesa
for idx,i in enumerate(data):
	if idx == 0:
		projected_coord.append(utils.project(i))
		continue
	print(str(idx) + " : " + str(i)) 
	projected_coord.append(utils.project(i))
	projected_coord_extended.extend(utils.explode_segment(utils.project(data[idx-1]), utils.project(i)))

print(projected_coord)

for i in projected_coord: 
	print(i)
	plt.plot(i[0],i[1],'ro')


for i in projected_coord_extended: 
	plt.plot(i[0],i[1],'bo')

plt.grid()
plt.show()
