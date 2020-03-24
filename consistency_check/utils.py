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
        """
        Returns the euclidean distance from two points
        """
        return np.sqrt( (pt2[0]-pt1[0])**2 +(pt2[1] - pt1[1])**2)

    def explode_segment(self, from_pt, to_pt, inter_distance=0.03):
        """ Creates a number of intermediate points from start to end
        """
        pt = []
        distance = self.distance(from_pt,to_pt)
        num_inter_points = int(distance/inter_distance)
        from_x = np.array([from_pt[0],from_pt[1]])
        to_x = np.array([to_pt[0],to_pt[1]])
        if num_inter_points == 0:
            pt.append(from_pt)
        if not distance%inter_distance == 0:
            rest = distance - num_inter_points*inter_distance
        for i in range(num_inter_points):
            if i == 0:
                # Check that maybe just pt.append(from_pt) should be ok
                pt.append(self.create_inter_points(from_x,to_x,i*(1.0/num_inter_points)))
                #pt.append(from_x)
            else:
                pt.append(self.create_inter_points(from_x,to_x,i*(inter_distance/distance)))
        return pt

    def create_inter_points(self, from_pt, to_pt, step):
        """
        Creates intermediate points
        """
        return (1-step)*from_pt + step*to_pt

    def project(self, coord):
        """
        Projection method to get planar coordinates from gps coordinates
        Apply geometric transformation
        """
        XX = np.radians(float(coord[0])-float(self.ref_point[0]))*6371*np.cos(np.radians(float(coord[1])))
        YY = np.radians(float(coord[1])-float(self.ref_point[1]))*6371
        return (XX,YY)

    def closest_node(self, pt, list_of_points):
        """
        Returns the index of the closest point in list_of_points to point pt
        """
        points = np.asarray(list_of_points)
        dist_2 = np.sum((points - pt)**2, axis=1)
        return np.argmin(dist_2)

    def closest_point_to_segment(self, start_x, start_y, end_x, end_y, pt):
        """
            Computes the solution to a minimization problem to find the closest
            point of a segment to a point. Closed form solution computation
        """
        t_star = pt[0]*(end_x - start_x) + pt[1]*(end_y - start_y) - end_x*start_x - end_y*start_y + start_x**2 + start_y**2
        # Compute closed form solution and clamp t* from [0,1] to handle points outside the segment
        t_star = self.constraint(  t_star / ( np.power(start_x - end_x,2) + np.power(end_y - start_y,2)) , 0, 1)
        # Compute the coordinates of the closest point of the arc to the pose
        pt_optimal = ( start_x + t_star*(end_x - start_x) , start_y + t_star*(end_y - start_y ))
        # Compute the distance
        dist = np.sqrt(( pt[0] - pt_optimal[0] )**2 + ( pt[1] - pt_optimal[1] )**2 )
        return (pt_optimal, dist)

    def constraint(self, n, minn, maxn):
        """
        Function to clamp a value n from [ minn, maxn]
        """
        return max(min(maxn, n), minn)
