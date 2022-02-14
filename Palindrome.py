import math 
"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.  A
permutation is a rearrangement of letters.  The palindrome does not need to be limited
to just dictionary words.  You can ignore casing and non-letter characters.
"""
lst = []
result = []

# Recursion to get all permutations combinations of a word
def getPermutations(word, pre=""):
    if (len(word) == 0):
        lst.append(pre)

        return pre 
    else:
        for i in range(len(word)):
            rem = word[:i] + word[i + 1:]
            getPermutations(rem, pre + word[i])


def checkPalindrome(check):
    for word in check:
        c = 0

        # Iterates through half the list of letters
        for i in range(int(len(word)/2)):
            # Checks if n letter is equal to -n
            if word[i] == word[-i-1]:
                c += 1
            
            # Checks if all the letters are equal, then adds to result
            if (c >= math.floor(len(word)/2)):
                if word not in result:
                    result.append(word)
    return result

# Replace removes all spaces within the string
getPermutations("taco cat".replace(" ", ""))
print(checkPalindrome(lst))