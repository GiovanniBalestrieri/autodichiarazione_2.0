# Consistency check

Aim: Given a path S and checkpoint position C, check whether the citizen being controled at C is too far away from the auto decleared path.
- Return true if current position is consistent with path, False otherwise

Inputs:
- The Path S is described by a sequence of coordinates in DD format.
- Checkpoint postion C in DD format.

Output:
- Boolean result of the consistency check

## Milestone 0

Describe the declared path as a sequence of planar coordinates

Given the Path S, apply a geometric transformation to all points in S. Apply a projection to get planar coordinates from point's coordinates in dd format

## Mileston 1

From a sequence of planar coordinates, create a sequence of intermediate equidistant points

Step 1 : From the sequence of projected points describing the path, create sequence of segments

Step 2 : From the sequence of projected segments, create intermediate equidistant points from the start of the segment to its end. 

 
## Milestone 2

Implement a function that returns the closest segment of the path to specific point in space. 
Basically, given a checkpoint control position C = (xc, yc), return the closest segment of the path to the control point C.

Starting from a simple case scenario with a path S described by two segments, create a function that returns the closest segment to the control point 

## Milestone 3

Implement a function that returns the closest point P* of the declared discretized path S to a specific point in space C.

## Milestone 4

Implement a function that given a Path S and a control point C, returns False if the distance between the control point C and the closest point P* of the path to C is greater than a threshold D. Returns True otherwise.


