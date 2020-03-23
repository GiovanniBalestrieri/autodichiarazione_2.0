#!/usr/bin/env python3
from utils import Utilities

# Setting POIs
home =  (5.712608, 45.176793)
mid_point = (5.709881, 45.177288)
market = (5.709441,45.176588)

utils = Utilities(market)

# Create path
path = [home, mid_point, market]

# Project coordinates 
home_p = utils.project(path[0])
mid_p = utils.project(path[1])
market_p = utils.project(path[2])

# Let's compute the distance between those two points
d1 = utils.distance(mid_p,market_p)

# Should be close to 90 m
print(d1)



