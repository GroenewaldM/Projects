print("Please think of a number between 0 and 100!")
hint = 0
guess = 50
low = 0
high = 100
    
while(hint != "c"):
    print("Is your secret number " + str(guess) + "?")
    
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if hint != "h" and hint != "l" and hint != "c":
        print("Sorry, I did not understand your input.")
    
    elif hint == "h":
        high = guess
        guess = int((low + high) / 2)
        
    elif hint == "l":
        low = guess
        guess = int((low + high) / 2)
    
        
        
print("Game over. Your secret number was: " + str(guess))