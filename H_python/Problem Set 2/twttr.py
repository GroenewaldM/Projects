string = input("Please enter string: ")
size = len(string)
i = 0

while i < len(string):
   
    if string[i].lower() == "a":
        string = string[:i] + string[i+1:]

    elif string[i].lower() == "e":
        string = string[:i] + string[i+1:]

    elif string[i].lower() == "i":
        string = string[:i] + string[i+1:]

    elif string[i].lower() == "o":
        string = string[:i] + string[i+1:]

    elif string[i].lower() == "u":
        string = string[:i] + string[i+1:]

    else:
        i = i + 1

print(string)
