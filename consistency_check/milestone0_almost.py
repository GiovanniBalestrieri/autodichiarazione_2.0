#!/usr/bin/env python3
from utils import Utilities
import json

# Load sequence of gps positions
with open('path.json') as f:
  data = json.load(f)

utils = Utilities(data[0])

projected_coord = []

# Project coordinatesa
for i in data:
	projected_coord.append(utils.project(i))



print(data)

print(projected_coord)

