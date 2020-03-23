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

Given the Path S, apply a geometric transformation to all points in S. Apply a projection to get planar coordinates from gps coordinates in dd format

## Mileston 1

From a sequence of planar coordinates, create a sequence of intermediate equidistant points
 
## Milestone 2

Implement a function that returns the closest point P* of the declared path S to a specific point in space C.

## Milestone 3

Implement a function that given a Path S and a control point C, returns False if the distance between the control point C and the closest point P* of the path to C is greater than a threshold D. Returns True otherwise.


