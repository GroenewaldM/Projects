math = input()
x = float(math[:math.find(" ")])
y = float(math[math.rfind(" "):])

if math[math.find(" ") + 1] == "+":
    print(x + y)

elif math[math.find(" ") + 1] == "-":
    print(x - y)

elif math[math.find(" ") + 1] == "*":
    print(x * y)

elif math[math.find(" ") + 1] == "/":
    print(x / y)