"""
Implement a method to perform a basic string compression using the counts of a repeated characters.
Examples: aabcccccaaa = a2b1c5a3.  If the compressed string would not become smaller than the original, your meothod
should return the original string.  You can assume the string only has upper and lower case letters (a-z)
"""

def compression(string):
    result = ""
    
    temp = ""
    swap = ""
    c = 0
    for j, i in enumerate(string):
        temp = i
        if (swap == "" or temp == swap):
            swap = temp 
            c += 1

        if (temp != swap):
            result = result + "{0}{1}".format(swap, c)
            c = 1
            swap = temp
        if (len(string) == (j+1)):
            result = result + "{0}{1}".format(temp, c)


    if (len(string) <= len(result)):
        return string
    
    return result

print(compression("tuuuuuuuutuu"))

