# Q- wap  to given data  of points which  x and y co-ordinates are given , those points are (1,2) ,  (1,3) , (2,4) , (5,7) these are co-ordinates of 4 pointsin 2D and its  origin position is (0,0)**
# >write functions to estimate distance between two points.

# >write function to estimate position of points in polar co-ordinates.

# >write function to move points when displacement is given.

import math

def distance (x1,x2,y1,y2):
    sq_distance=(x2-x1)**2 + (y2-y1)**2
    total_distance=sq_distance**(1/2)
    return total_distance
point1=(1,2)
point2=(2,3)
dist = distance(point1[0],point1[1],point2[0],point2[1])
print(f"the distance between two points{point1}and {point2} is {dist }")
    
    