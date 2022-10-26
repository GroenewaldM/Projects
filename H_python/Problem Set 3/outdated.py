i = 1
flag = 0
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while flag == 0:
    date = input("Date: ").title()
    date_list = date

    for d in date:
        if d == "/":
            date_list = date.split("/")
            day = date_list[1].split(",")
            dd = int(day[0])
            mm = int(date_list[0])
            if 0 < mm < 13 and 0 < int(dd) < 32:
               flag = 1

        elif date[0].isalpha():
            date_list = date.split(" ")
            day = date_list[1].split(",")
            dd = int(day[0])

    i = 1    
    for m in month:
        if date_list[0] == m and 0 < int(dd) < 32:
            mm = i
            flag = 1
        else:
            i = i + 1             

    YYYY = date[len(date)-4:]
print(YYYY, "-", f"{mm:02}", "-", f"{dd:02}", sep = "")
