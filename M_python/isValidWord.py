def isValidWord(word, hand, wordList):
    hand_copy = hand.copy()
    
    for letter in word:
        
        if letter not in hand:
            return False
        elif hand_copy[letter] <= 0:
            return False
        else:
            hand_copy[letter] -= 1
            
    if word in wordList:
        return True
    else:
        return False
    
print(isValidWord("dogg", {'d': 1, 'o': 1, 't': 1, 'g': 1, 'a': 3, 'u': 1}, ["dogg", "cat", "raptue"]))