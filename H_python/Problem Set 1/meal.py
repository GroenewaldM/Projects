def main():
    hhmm = input("What is the time? ")
    if convert(hhmm) >= 7 and convert(hhmm) <= 8:
        print("breakfast time")

    elif convert(hhmm) >= 12 and convert(hhmm) <= 13:
        print("lunch time")

    elif convert(hhmm) >= 18 and convert(hhmm) <= 19:
        print("dinner time")


def convert(time):

    hh = float(time[:time.find(":")])
    mm = float(time[time.find(":") + 1: time.find(":") + 3])

    if time.endswith("p.m.") and hh != 12:
        return hh + 12 + (mm / 60)
    elif time.endswith("a.m.") and hh == 12:
        return hh - 12 + (mm / 60)
    else:
        return hh + (mm / 60) 

main()