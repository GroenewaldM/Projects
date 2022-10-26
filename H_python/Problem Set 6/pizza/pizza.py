import sys
from tabulate import tabulate
data = []

if len(sys.argv) < 2:
    print("No command line argument!")
    sys.exit()

elif len(sys.argv) > 2:
    print("Too many command line arguments!")
    sys.exit()

else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                data.append(line.rstrip().split(","))
    
    except FileNotFoundError:
        print("File not found!")
        sys.exit()

print(tabulate(data[1:6], data[0], tablefmt="grid"))

