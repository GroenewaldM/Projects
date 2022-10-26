from validator_collection import validators

value = input("test:")

try:
    validators.email(value, allow_empty = True)
    print("Valid")

except ValueError:
    print("Invalid")