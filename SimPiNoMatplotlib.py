import math
import random

inside = 1
outside = 1
count = 0

def inCircle(x, y):
    #function that sees if the coordinates are contained within the circle, either returning false or true
    return math.sqrt( (x**2) + (y**2) ) <= 1

while True:
    count = count + 1
    #random.uniform generates a 'random' number between the given values, for example, 'random.uniform(-1, 1)' generates .21946219
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    #if its in the circle, add one to the amount of points inside the circle
    if (inCircle(x, y)):
        inside = inside + 1
    #and one if the coordinate is not in the circle
    else:
        outside = outside + 1
    #this prints the ratio of coordinates inside the circle with the points outside the circle
    #each 100 is printed to reduce the amount of clutter
    if count % 100:
        print(inside / outside)
