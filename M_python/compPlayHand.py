def updateHand(hand, word):
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1

    return hand_copy

def compPlayHand(hand, wordList):
    hand_copy = hand.copy()
    comp_answer = ""
    for words in wordList:
        for letter in words:
            if letter in hand_copy and hand_copy[letter] > 0:
                hand_copy[letter] -= 1
                correct = 1
            else:
                correct = 0
                hand_copy = hand.copy()
        if correct == 1 and len(words) > len(comp_answer):
            comp_answer = words 
            correct = 0
            

            
    return comp_answer                       
print(compPlayHand({'d': 1, 'o': 1, 't': 1, 'g': 2, 'a': 3, 'u': 1}, ["dog", "dogg", "cat", "raptue"]))