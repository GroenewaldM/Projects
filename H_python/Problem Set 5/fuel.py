def main():
    fuel_fraction = input("Fraction: ")
    argument = (gauge(convert(fuel_fraction)))
    print(argument)


def gauge(percentage):
    if percentage[0] == "0" and percentage[1] != "0":
        return "E"

    elif percentage[0] == percentage[1] and percentage[0] != "0":
        return "F"

    else:
        return f"{int(int(percentage[0]) / int(percentage[1]) * 100)}" + " %"


def convert(fraction):
    while True:
        try:
            fuel_percentage = fraction.split("/")
            if int(fuel_percentage[0]) <= int(fuel_percentage[1]):
                return fuel_percentage
            else:
                fraction = input("Fraction: ")

        except ValueError:
            fraction = input("Fraction: ")
        except IndexError:
            fraction = input("Fraction: ")

if __name__ == "__main__":
    main()

