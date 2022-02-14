"""
There are three edits you can do to a string: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they were one edit (or zero edits) away.
"""

def checkStrings(a, b):
    if (a == b): return True

    short = ""
    long = ""
    
    if (len(a) > len(b)):
        short = b
        long = a
    else:
        short = a
        long = b

    c = 0

    for i in range(len(long)):
        for j in range(len(short)):
            if long[i] == short[j]:
                c += 1
    
    if (c >= len(long) - 1) and (len(long) - len(short) <= 1):
        return True
    else:
        return False

print(checkStrings("pales", "ales"))