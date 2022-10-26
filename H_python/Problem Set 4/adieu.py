name = []
while True:
    try:
        name.append(input("Name: "))
    except EOFError:
        print("Adieu, adieu, to", end="")
        for i in range(len(name)):
            if i == len(name) - 2:
                print(" ", name[i], " and", end="", sep="")
            elif i == len(name) - 1:
                print(" ", name[i], end="", sep="")
            else:
                print(" ", name[i], ",", end="", sep="")
        break
