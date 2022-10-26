def shift(word, shift_value):

    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift_dict = {}
    encripted_word = ""

    for i in range(len(alpha)):
        try:
            shift_dict[alpha[i]] = alpha[i + shift_value]
        except IndexError:
            i = i - 26
            shift_dict[alpha[i]] = alpha[i + shift_value]
            
    for i in range(len(ALPHA)):
        try:
            shift_dict[ALPHA[i]] = ALPHA[i + shift_value]
        except IndexError:
            i = i - 26
            shift_dict[ALPHA[i]] = ALPHA[i + shift_value]
    
    for letter in word:
        if letter in shift_dict:
            encripted_word += (shift_dict[letter])
        else:
            encripted_word += (letter)
    return encripted_word
            
encripted_string = "khoor krz duh brx"
valid_words = ["hello", "you", "me"]
n = 0
n_updated = 0
message = ""
for s in range(1, 27):
    n_updated = 0
    message = ""
    shift_value = 26 - s 
    encripted_words = shift(encripted_string, shift_value)
    words = encripted_words.split(" ")
            
    for word in words:
        if word in valid_words:
            n_updated = (n_updated + 1)
        message += word
        message += " "
        
    if n < n_updated:
        n = n_updated
        answer_message = message
        answer = s
print(answer)
print(answer_message)
