import sys
import random
from pyfiglet import Figlet

f = input("Font input: ")
figlet = Figlet()

if len(f) == 0:
    f = random.choice(figlet.getFonts())

try:
    if f in figlet.getFonts():
        figlet = Figlet(font=f)

    else:
        sys.exit()
except SystemExit:
    print("Invalid font!")
    sys.exit()

string = input("Input: ")
print("Output:", "\n", figlet.renderText(string))
