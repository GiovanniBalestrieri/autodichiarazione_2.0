#!/usr/bin/env python3
from utils import Utilities
import json

# Load sequence of gps positions
with open('path.json') as f:
  data = json.load(f)

utils = Utilities(data[0])

projected_coord = []

# Project coordinatesa
for idx,i in enumerate(data):
	if idx == 0:
		pass
	print(str(idx) + " : " + str(i)) 
	projected_coord.extend(utils.explode_segment(utils.project(data[idx-1]), utils.project(i)))


print(len(data))
print(len(projected_coord))


