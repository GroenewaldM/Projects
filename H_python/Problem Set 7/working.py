import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search("^([0-9]{1}|[10,11,12]{2})(:([0-5][0-9]))? AM to ([0-9]{1}|[10,11,12]{2})(:([0-5][0-9]))? PM", s): 
        if matches.group(1) == "12":
            hh_start = 0
        else:
            hh_start = int(matches.group(1))

        if matches.group(3) == None:
            mm_start = 0
        else:
            mm_start = int(matches.group(3))

        if matches.group(4) == "12":
            hh_end = 12
        else:
            hh_end = int(matches.group(4)) + 12

        if matches.group(6) == None:
            mm_end = 0
        else:
            mm_end = int(matches.group(6))

        return f"{hh_start:02}:{mm_start:02} to {hh_end:02}:{mm_end:02}"

    elif matches := re.search("^([0-9]{1}|[10,11,12]{2})(:([0-5][0-9]))? PM to ([0-9]{1}|[10,11,12]{2})(:([0-5][0-9]))? AM", s):
        if matches.group(1) == "12":
            hh_start = 12
        else:
            hh_start = int(matches.group(1)) + 12

        if matches.group(3) == None:
            mm_start = 0
        else:
            mm_start = int(matches.group(3))

        if matches.group(4) == "12":
            hh_end = 0
        else:
            hh_end = int(matches.group(4))

        if matches.group(6) == None:
            mm_end = 0
        else:
            mm_end = int(matches.group(6))

        return f"{hh_start:02}:{mm_start:02} to {hh_end:02}:{mm_end:02}"

    else:
        return "Not correct format"



if __name__ == "__main__":
    main()