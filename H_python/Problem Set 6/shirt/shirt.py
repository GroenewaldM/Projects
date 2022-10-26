import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    print("Too few command line arguments")
    sys.exit()

elif len(sys.argv) > 3:
    print("Too many command line arguments")
    sys.exit()

elif sys.argv[1].endswith(".gif") == False and sys.argv[1].endswith(".jpg") == False and sys.argv[1].endswith(".png") == False:
    print("Invalid output")
    sys.exit()

elif sys.argv[2].endswith(".gif") == False and sys.argv[2].endswith(".jpg") == False and sys.argv[2].endswith(".png") == False:
    print("Invalid output")
    sys.exit()

elif sys.argv[1][-4:] != sys.argv[2][-4:]:
    print("Input and output have different extensions")
    sys.exit()

else:
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = ImageOps.fit(Image.open(sys.argv[1]), size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit()
    