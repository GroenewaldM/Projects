import sys
import csv

title = "name,house\n"
new_title = "first name, last name, house\n"
students = []

if len(sys.argv) < 3:
    print("Too few command line arguments!")
    sys.exit()

elif len(sys.argv) > 3:
    print("Too many command line arguments!")
    sys.exit()

else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for full_name, house in reader:
                if full_name != "name":
                    last, first = full_name.split(",")
                    students.append({"first name": first, "last name": last, "house": house})

        with open(sys.argv[2], "a") as file:
            file.write(new_title)
            for student in students:
                file.write(f'{student["first name"]}, {student["last name"]}, {student["house"]}\n')
    
    except FileNotFoundError:
        print("File not found!")
        sys.exit()


