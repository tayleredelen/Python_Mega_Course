# Write a program that:
# 1. asks users to enter a password.
# 2. returns "Great password there!" if the password has more than 7 characters.
    # For example:
    # Enter a new password: mycool_password3001
    # Great password there!
# 3. returns "Your password is weak." if the password has 7 or fewer characters.
    # For example:
    # Enter a new password: 1234
    # Your password is weak

# Solution
# password = input("Enter a password: ")
# if len(password) >= 7:
#     print("Great password there!")
# else:
#     print("Your password is weak")


# Write a program that:
# 1. asks users to enter a password.
# 2. returns "Great password there" if the password has more than 7 characters.
# 3. returns "Password is OK, but not too strong" if the password has exactly 7 characters.
# 4. returns "Your password is weak" if the password has 7 or fewer characters.

# Solution
# password = input("Enter a password: ")
# if len(password) > 7:
#     print("Great password there!")
# elif len(password) == 7:
#     print("Password is OK, but not too strong")
# else:
#     print("Your password is weak")

# Assign a dictionary to variable day_temperatures.
# The dictionary should contain three keys, 'morning', 'noon', and 'evening'
# Each key should have a float as value

# Solution
# day_temperatures = {'morning': 1.1, 'noon': 2.2, 'evening': 3.3}


# Assign a dictionary to variable day_temperatures.
# The dictionary should contain three keys: 'morning', 'noon', and 'evening'
# and each key should contain a tuple as a value. Each tuple should contain three floats.

# Solution
# day_temperatures = {'morning': (1.1, 2.2, 3.3), 'noon': (4.4, 5.5, 6.6), 'evening': (7.7, 8.8, 9.9)}


# Print out the slice ['b', 'c', 'd'] of the letters list using slicing.

# Solution:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[1:4])


# Print out the slice ['a', 'b', 'c'] of the letters list using slicing.

# Solution:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[0:3])


# Print out the slice ['e', 'f', 'g'] of the letters list using slicing.

# Solution:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[4:7])