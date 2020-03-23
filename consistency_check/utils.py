#!/usr/bin/env python3
# coding: utf-8
import numpy as np

__version__ = "0.1"
__author__ = "Giovanni Balestrieri"


##
#   Utility class
##
class Utilities:
	def __init__(self, ref):
	        self.ref_point = ref

	def distance(self, pt1, pt2):
		return np.sqrt( (pt2[0]-pt1[0])**2 +(pt2[1] - pt1[1])**2)
	
	def explode_segment(self, from_pt, to_pt, inter_distance=10):
		pass

	def create_inter_points(self, from_pt, to_pt, step):
		return (1-step)*from_pt + step*to_pt

	def project(self, coord):
		""" Second method to apply projection to get planar 
		    coordinates from point's coordinates in dd format
	            Apply geometric transformation
 	       """
		XX = np.radians(float(coord[0])-float(self.ref_point[0]))*6371*np.cos(np.radians(float(coord[1])))
		YY = np.radians(float(coord[1])-float(self.ref_point[1]))*6371
		return (XX,YY)
