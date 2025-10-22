# A list of coordinate tuples and a function to calculate distances.

import math 
points = ((0,0),(2,4),(6,8),(10,12))

def calculate_distance(p1,p2):
    return math.dist(p1,p2)  #distance = √[(x₂ - x₁)² + (y₂ - y₁)²]

print("Distances betwen 2nd and 3rd points : ",calculate_distance(points[1],points[2]))
print()