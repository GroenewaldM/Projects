
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    l = len(aStr)
    low = 0
    high = l

    if l < 1:
        return False
    
    elif char == aStr[int(l/2)]:
        return True
    
    else:    
        if l <= 1:
            return False
        
        elif char < aStr[int(l/2)]:
            high = int(l/2)
            return isIn(char, aStr[low:high])

        else:
            low = int(l/2)
            return isIn(char, aStr[low:high])
        

    
a = isIn("a", "")
print(a)
