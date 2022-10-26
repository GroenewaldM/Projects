import sys
i = 0

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as file:
                for line in file:
                    if  line == "\n" or (line.startswith("# ")):
                        pass

                    else:
                        i = i + 1
    except FileNotFoundError:
        print("File not found")
        sys.exit()

elif len(sys.argv) < 2:
    print("No command line argument")
    sys.exit()

else: 
    print("Too many command line arguments")
    sys.exit()
    
print(i)
    