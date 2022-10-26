import sys

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
            for line in file:
                if line != title:
                    fullname, house =(line.rstrip().split('",'))
                    last, first = fullname.lstrip('"').split(",")
                    student = {"first name": first, "last name": last, "house": house }
                    students.append(student)

        with open(sys.argv[2], "a") as file:
            file.write(new_title)
            for student in students:
                file.write(f'{student["first name"]}, {student["last name"]}, {student["house"]}\n')
    
    except FileNotFoundError:
        print("File not found!")
        sys.exit()


