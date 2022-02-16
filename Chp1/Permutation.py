
# def checkPermutation(a, b):

#     if (len(a) < len(b)):
#         for i in range(len(a)):
#             for j in range(len(a)):
#                 if (a[i] == b[j]):
                    
        
#         return 
#     else:
#         pass

#     return a, b



# print(checkPermutation("tes", "testing"))




lst = []



def permutations(word, pre): #takes two strings
    if (len(word) == 0):
        lst.append(pre)
        return pre

    else:
        for i in range(len(word)):
            rem = word[:i] + word[i + 1:]
            permutations(rem, pre + word[i])


def checkPermutation(a, b):
    if (len(a) < len(b)):
        permutations(a, "")

    elif (len(b) < len(a)):
        permutations(b, "")
    
    for sub in lst:
        if sub in b:
            print("Yes, " + sub)


checkPermutation("est", "Oustestdfjkdfjazieststse")