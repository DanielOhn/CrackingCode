"""
Write an algorithm such that if an element in an 
M x N matrix is 0, its entire row and col are set to 0.
"""
def setZero(matrix):
    newMatrix = []
    zeros = {"rows": [], "cols": []}

    # Get Location of all Zeros in the Matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 0):
                print("({0}, {1})".format(i, j))
                zeros["rows"].append(i)
                zeros["cols"].append(j)

    # Iterates through matrix again and places Zeros in the correct place
    for i in range(len(matrix)):
        newMatrix.append([])
        for j in range(len(matrix[i])):
            if (i in zeros["rows"] or j in zeros["cols"]):
                newMatrix[i].append(0)
            else:
                newMatrix[i].append(matrix[i][j])

    return newMatrix

def printM(m):
    for i in m:
        print(*i)

mat = [[1,2,3],[5,0,6],[7,8,9]]
zero = setZero(mat)

printM(mat)
print("----")
printM(zero)
