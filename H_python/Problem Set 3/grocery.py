n = 0
grocery_dict = {}

while True:
    try:

        item = input().upper()

        if item in grocery_dict:
            n = n + 1
            grocery_dict.update({item:grocery_dict[item] + 1})
           
        else:
            n = 1
            grocery_dict.update({item:n})

    except EOFError:
        for item in grocery_dict:
            print(grocery_dict[item], item)
        break
                  
  
            