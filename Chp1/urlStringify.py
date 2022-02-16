"""
Write a method to replace all spaces in a string with "%20".
You may assume that the string has sufficient space at the end to held the additional characters, and that you are gien the 'true' length of hte string.
EX: "Mr John Smith.....  ", 13
"""

def urlify(url, num):

    newUrl = []

    for count, letter in enumerate(url[:num]):
        if (letter == " "):
            newUrl.append("%20")
        else:
            newUrl.append(letter)

    return "".join(newUrl)
    
print(urlify("Mr John Smith    ", 13))