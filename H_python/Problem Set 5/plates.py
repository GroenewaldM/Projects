def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(s):
 i = 0

 if 1 < len(s) <7 and s[:1].isalpha() and s.isalnum():

    while i < len(s):

         if  s[i].isnumeric():
             break

         else:
            i = i + 1

    if (s[i:].isnumeric() and s[i] != "0") or s.isalpha():
        return "Valid"

    else:
        return "Invalid"

 else:
    return "Invalid"


if __name__ == "__main__":
    main()
