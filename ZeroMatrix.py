"""
Write an algorithm such that if an element in an 
M x N matrix is 0, its entire row and col are set to 0.
"""
def setZero(matrix):
    newMatrix = []
    zero = False
    for i in range(len(matrix)):
        newMatrix.append([])
        zero = False
        for j in matrix[i]:
            if j == 0:
                newMatrix[i].append(0)
                zero = True
                if (i > 0):
                    newMatrix[i-1].pop()
                    # newMatrix[i-1].append(0)
            elif j != 0 and zero:
                newMatrix[i].append(0)
            else: 
                newMatrix[i].append(j)

    return newMatrix



def matrix(m, n):
    lst = []
    for i in range(m):
        lst.append([])
        for j in n:
            lst[i].append(j)
    
    return lst 

def printM(m):
    for i in m:
        print(*i)

mat = matrix(3, [1, 0, 3, 5])
zero = setZero(mat)

printM(mat)
print("----")
printM(zero)
