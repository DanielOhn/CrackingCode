""" 
A child is running up a staircase with n steps and can hop either 1 step, 2 step, or step at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""
def TripleStep(n):
    if (n == 0):
        return 1
    elif (n < 0):
        return 0
    else:
        return TripleStep(n - 3) + TripleStep(n - 2) + TripleStep(n - 1)

step = TripleStep(5)
print(step)