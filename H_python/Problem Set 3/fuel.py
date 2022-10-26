while True:
   
    try:
        fraction = input("Please enter fuel fraction: ")
        percentage = fraction.split("/")
        if int(percentage[0]) <= int(percentage[1]):
            break

    except ValueError:
        pass

if percentage[0] == "0" and percentage[1] != "0":
        print("E")

elif percentage[0] == percentage[1] and  percentage[0] != "0" :
        print("F")

else:
    print(int(int(percentage[0])/int(percentage[1])*100) , "%")
