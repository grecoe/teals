'''
    Using named tuples (to play with)....
    Given a grid full of points with x,y coordinates, find all of the rectangles 
    that exist within the given set of points. 

    Grid1 - 3 rectangles 
    (0,2)   (2,2)   (4,2)
      *       *       *

    (0,0)   (2,0)   (4,0)
      *       *       *

    Grid2 - 2 Rectangles
            (2,3)            (6,3)
    (0,2)      *   (4,2)       *
      *              *

            (2,1)            (6,1)
    (0,0)     *    (4,0)       *
      *              *
'''
from collections import namedtuple

Point = namedtuple("Point", "x y")
Line = namedtuple("Line", "start end")
Rectagle = namedtuple("Rectangle", "x1, x2, x3, x4")

# First grid - 3 rectangles
grid1 = [
    Point(x=0, y=0),
    Point(x=0, y=2),
    Point(x=2, y=0),
    Point(x=2, y=2),
    Point(x=4, y=0),
    Point(x=4, y=2)
]


# Second grid - 1 rectangles
grid2 = [
    Point(x=0, y=0),
    Point(x=0, y=2),
    Point(x=2, y=1),
    Point(x=2, y=3),
    Point(x=4, y=0),
    Point(x=4, y=2),
    Point(x=6, y=1),
    Point(x=6, y=3)
]

'''
    Line end needs to be further down the x-axis and both start and end y points must 
    align to be right angled.
'''
def linesAreParallel(lineStart, lineEnd ):
    if (lineStart.start.x > lineEnd.start.x) and (lineStart.start.y == lineEnd.start.y) and (lineStart.end.y == lineEnd.end.y):
        return True
    return False

'''
    Process to determine how many rectangles are on it. 
    1. Find all vertical lines
    2. Compare each line with the other lines (assuming it lies further down the x axis)
       to see if they form a rectangle (y coords line up on start/end line)
'''
def processGrid(grid):
    # Find all the vertical lines in this list
    verticallines = []
    rectangles = []
    for point in grid:
        for point2 in grid:
            if point.x == point2.x and point.y < point2.y:
                # We have a vertical line, save it....
                verticallines.append(Line(start = point, end = point2))

    # Now using list comprehension combined with a function, to
    # find number of rectagles. 
    rect_count = 0
    for line in verticallines:
        future_points = [x for x in verticallines if linesAreParallel(x, line)]
        rect_count += len(future_points)
        for future in future_points:
            rectangles.append(Rectagle(x1 = line.start, x2 = line.end, x3 = future.start, x4 = future.end))


    print("There are", len(verticallines), "vertical lines and ", rect_count, "rectangles.")
    for rect in rectangles:
        print(rect)

'''
    Calls to process our grids
'''
print("Grid1")
processGrid(grid1)
print("Grid2")
processGrid(grid2)