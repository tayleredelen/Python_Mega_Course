from ToDoApp.Day14.converters14 import convert
from ToDoApp.Day14.parsers14 import parse

feet_inches = input("Enter feet an inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")