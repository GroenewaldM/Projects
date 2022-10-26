def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in lettersGuessed:
        if letter not in secretWord:
            return False
        
    return True

secretWord = 'apple' 
lettersGuessed = ['p', 'a', 'l', 'l', 'e']
print(isWordGuessed(secretWord, lettersGuessed))

isWordGuessed(secretWord, lettersGuessed)