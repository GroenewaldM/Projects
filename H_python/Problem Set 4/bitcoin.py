import json
import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit()
except NameError:
    print("Command-line argument is not a number")
    sys.exit()
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
amount = n * float(response["bpi"]["USD"]["rate_float"])
print(f"${amount:,.4f}")
