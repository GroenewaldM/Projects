def main():
    word = input("Word: ")
    shorten(word)

def shorten(string):
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
    return string

if __name__ == "__main__":
    main()