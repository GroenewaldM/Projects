import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^\d+\.\d+\.\d+\.\d+$", ip):
        a, b, c, d = ip.split(".")
        if int(a) < 256 and int(b) < 256 and int(c) < 256 and int(d) < 256:
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()