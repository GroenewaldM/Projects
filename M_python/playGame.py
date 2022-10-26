        
def getWordScore(word, n):
    
    scrabble_values_dict = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4,
    "i":1, "j":8, "k":5,"l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, 
    "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
    word_length = len(word)
    letter_score = 0
    letter_count = 0
    word = word.lower()
    
    for letter in word:
        letter_score += scrabble_values_dict[letter]
        letter_count += 1
    
    if letter_count == n:
        return letter_score * word_length + 50
    else:
        return letter_score * word_length

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

def updateHand(hand, word):
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1

    return hand_copy 

def playHand(hand, wordList, n):
    
    word = ""
    total_points = 0
    updated_hand = hand.copy()
    
    while True:
        current_hand = ""
        for letter in updated_hand:
            for _ in range(int(updated_hand[letter])):
                current_hand += (letter + " ")
        
        if len(current_hand) == 0:
            print(f"Run out of letters. Total score: {total_points} points.")
            break
        if word == ".":
            print(f"Goodbye! Total score: {total_points} points") 
            break
        else:
            print(f"Current hand: {current_hand}")
            word = input('Enter word, or a "." to indicate that you are finished: ')
        
            if isValidWord(word, updated_hand, wordList):
                points = getWordScore(word, n)
                total_points = total_points + getWordScore(word, n)
                updated_hand = updateHand(updated_hand, word)
                print(f'"{word}" earned {points} points. Total: {total_points} points')
            elif  word != ".":
                print("Invalid word, please try again.")
        
def playGame(wordList):
    response = ""
    while True:
        n = 7
        response = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if response == "n":
            hand = {'d':1, 'i':1, 'o':1, 'z':1, 'g':2, 'a':1} #dealHand()  
            playHand(hand, wordList, n)
        elif response == "r":
            try:
                playHand(hand, wordList, n)
            except UnboundLocalError:
                print("You have not played a hand yet. Please play a new hand first!")
        elif response == "e":
            break
        else:
            print("Invalid command.")
        

wordList = ["dog", "cat", "hi", "dogg", "iz", "a"]
(playGame(wordList))
        