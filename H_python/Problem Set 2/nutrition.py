fruits = {"apple":"130", "avocado":"50", "banana":"110", "caunaloupe":"50",
"grapefruit":"60", "grapes":"90", "honeydew melon":"50", 
"kiwifruit":"90", "lemon":"15", "lime":"20", "Nectarine":"60", 
"orange":"80", "peach":"60", "pear":"100", "pineapple":"50", 
"plum":"70", "strawberry":"50", "sweet cherries":"100", "Tangerine":"50", 
"watermelon":"80"}

f = input("Fruit: ").lower()

if f in fruits:
    print("Calories:" , fruits[f])