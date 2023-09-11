# We have a list of three strings defined in the code area.
# Extend the code so your program prints out the following out of that list:
# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

# Solution:
# filenames = ['document', 'report', 'presentation']
# for index, item in enumerate(filenames):
#     row = f"{index}-{item.capitalize()}.txt"
#     print(row)


# We have a list of two IPs in the code area.
# Extend the code so your program:
# 1. Prompts the user to input an index (e.g., 0 or 1).
# 2. Depending on the user input, the program should return either
# You chose 100.122.133.111 or You chose 100.122.133.111
# Note: In order for the system to mark your exercise as correct, your code should return the exact output
# (i.e., upper case Y in You chose and no spaces or other characters after the IP.
# For example:
# Enter the index of the IP you want: 1
# You chose 100.122.133.111

# Solution:
# ips = ['100.122.133.105', '100.122.133.111']
# user_choice = int(input("Enter the index of the IP you want: "))
# message = f"You chose {ips[user_choice]}"
# print(message)


# Assign a list to the variable temperatures.
# The list should contain three items, a float, an integer, and a string.

# Solution:
# temperatures = [3.14, 1, "weather"]


# Assing a list to the rainfallvariable.
# The list should contain four items, a float, an integer, a string, and a list*.
# *It's totally fine for a list to contain another list as an item.

# Solution:
# rainfall = [3.14, 1, "weather", [1, 2, 3]]


# Remove item 1.45 from seconds.

# Solution:
# seconds = [1.23, 1.45, 1.02, 1.11]
# seconds.remove(1.45)
# print(seconds)

