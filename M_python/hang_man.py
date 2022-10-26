def HangMan(word):
    
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    word_length = len(word)
    display_word = ""
    correct = 0
    display_dict = {}
    number_guesses = 8
    
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {word_length} letters long.")
    print("------------")
    
    for i in range(word_length):
        display_dict[i] = "_ "
   
    while display_word != word and number_guesses > 0: 
        
        correct = 0
        display_word = ""
        position = 0
        
        if number_guesses == 1:
            print(f"You have {number_guesses} guess left.")
        else:
            print(f"You have {number_guesses} guesses left.")
        
        print("Available letters: " + str(available_letters))
        guess = input("Please guess a letter: ").lower()
        
        for letter in word:
            if guess == letter and guess in available_letters:
                display_dict[position] = letter
                correct = 1

            display_word += (display_dict[position])
            position += 1
            
        if guess not in available_letters:
            correct = 2
        
        available_letters = available_letters. replace(guess, "")
        
        if correct == 1:
            print("Good Guess: " + str(display_word))    
        elif correct == 0:
            print("Oops! That letter is not in my word: " + str(display_word))
            number_guesses -= 1
        else:
            print("Oops! You've already guessed that letter: " + str(display_word))
            
        print("------------")
        
    if number_guesses == 0:
        print(f"Sorry, you ran out of guesses. The word was {word}. ")
    else:
        print("Congratulations, you won!")
        
                
HangMan("yessus")