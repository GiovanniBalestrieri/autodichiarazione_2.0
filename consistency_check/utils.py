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

    def explode_segment(self, from_pt, to_pt, inter_distance=0.01):
        """ Creates a number of intermediate points from start to end
        """
        pt = []
        distance = self.distance(from_pt,to_pt)
        num_inter_points = int(distance/inter_distance)
        if not distance%inter_distance == 0:
            rest = distance - num_inter_points*inter_distance
        for i in range(num_inter_points):
            from_x = np.array([from_pt[0],from_pt[1]])
            to_x = np.array([to_pt[0],to_pt[1]])
            if i == 0:
                # Check that maybe just pt.append(from_pt) should be ok
                pt.append(self.create_inter_points(from_x,to_x,i*(1.0/num_inter_points)))
            else:
                pt.append(self.create_inter_points(from_x,to_x,i*(inter_distance/distance)))
        return pt

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
