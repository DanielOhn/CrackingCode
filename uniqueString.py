def stringCheck(string):
    for i in range(len(string)):
        for j in string[i+1:]:
            if string[i] == j:
                #print(string[i], j)
                return False    
    return True


print(stringCheck("jaming"))