'''
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are 'off limits'
such that the robot can't step on them.  Design an algorithm to find a path for the robot from the top left
to the bottom right.
'''

def robotMaze(r, c):
    if (r <= 1 or c <= 1 or r-1 == "off limits" and c-1 == "off limits"):
        return 1
    
    if (r-1 == "off limits"):
        return robotMaze(r, c-1)
    elif (c-1 == "off limits"):
        return robotMaze(r-1, c)
 
    return robotMaze(r-1, c) + robotMaze(r, c-1)
