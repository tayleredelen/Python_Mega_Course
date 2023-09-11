# The given code is incomplete. Your task is to continue that program.
# You need to:
# 1. calculate the percentage using the  value/total * 100 formula
# 2. print out, for example, "That is 40.0%" as shown in the sample below:
    # Enter total value: 50
    # Enter value: 20
    # That is 40.0%
# The program should also print a message if the user doesn't enter a number
# for the "total value or for the "value":
    # Enter total value: 20
    # Enter value: hi
    # You need to enter a number. Run the program again.

# Solution:
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     result = float((value / total_value) * 100)
#     print(f"That is {result}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")


# As you might know, it is not mathematically possible to divide a number
# by zero. Consequently, this is also not possible in Python either -you
# will get a ZeroDivisionError if you try:
    # >>> 20 / 0
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # ZeroDivisionError: division by zero
# With that in mind, your task for this exercise is to extend the program you
# created in Exercise 1 by displaying a message to the user when they enter 0 for the "total value".
    # Enter total value: 20
    # Enter value: hi
    # Your total value cannot be zero.

# Solution:
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     if total_value == 0:
#         print("Your total value cannot be zero")
#         exit()
#     result = float((value / total_value) * 100)
#     print(f"That is {result}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")


# Loop over the colors items and print out the item in every loop only if the item is greater than 50.
# So, the output of your program would be:
#     98
#     54
#     54

# Solution:
# colors = [11, 34, 98, 43, 45, 54, 54]
# for i in colors:
#     if i > 50:
#         print(i)
