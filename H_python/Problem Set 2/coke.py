price = 50
value = 0
left = price - value

print("Amount due:", price)

while left > 0:
    value = int(input("Insert coin: "))
    if value == 5 or value == 10 or value == 25:
        left = left - value
    if left > 0:
            print("Amount due:", left)
   
if left <= 0:
        print("Change owed:", 0 - left)