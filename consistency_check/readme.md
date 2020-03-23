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

Step 0 : Apply a geometric transformation to all points in the path. Apply a projection to get planar coordinates from point's coordinates in dd format

 

