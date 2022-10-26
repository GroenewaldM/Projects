
name = input("Please enter variable name: ")
i = 0
n = 0
snake_name = name
if name.islower():
    print(name)  
else :
    while i < int(len(name)): 
        if name[i].isupper():
            snake_name = snake_name[:n] + "_" + snake_name[n:]
            n = n + 1
        i = i + 1 
        n = n + 1
  
    print(snake_name.lower())         
        
        

