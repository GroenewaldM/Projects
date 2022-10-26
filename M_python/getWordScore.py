
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
        

print(getWordScore('triplet', 8))