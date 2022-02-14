"""
Given an image represented by an N x N matrix, where each pixel is the image is represented by an integer, write a method
to rotate the image by 90 degrees.  Can you do this in place?
"""

def matrixRotate(m):
    rotate = []
    for i in range(len(m)):
        rotate.append([])
        for j in reversed(range(len(m))):
            rotate[i].append(m[j][i])
    
    return rotate


def createMatrix(n):
    temp = []
    c = 0
    for i in range(n):
        temp.append([])
        for j in range(n):
            temp[i].append(c)
            c += 1
    
    return temp

matrix = createMatrix(4)

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])

printMatrix(matrix)
print("New Matrix")

rotated = matrixRotate(matrix)
printMatrix(rotated)