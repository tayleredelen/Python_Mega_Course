# On the side panel there's a bear.txt file.
# The existing code opens that file in read mode.
# Below that code, please read the file content and print out the content.

# Solution:
# file = open("bear.txt")
# content = file.read()
# print(content)


# Take a loot at the essay.txt file tab. That file contains some text.
# You should create a program that reads the essay.txt file,
# converts the first letter of each word to uppercase and prints out
# the converted text.

# Solution:
# file = open("essay.txt", 'r')
# for line in file:
#     l=line.title()
#     print(l)


# Write a program that reads the essay.txt file and returns the number
# of characters contained in the file.

# Solution:
# file = open("essay.txt", 'r')
# num_char = file.read()
# chars = len(num_char)
# print(chars)


# Use Python to create a file with name file.txt and write the text snail there.

# Solution:
# file = open('file.txt', 'w')
# content = 'snail'
# file.write(content)
# file.close()


# For this exercise, download the members.txt file attached to the resources.
# Then, create a program that:
# 1. prompts the user to enter a new member.
# 2. adds that member to members.txt at the end of the existing members.
# For example, the user here has entered the member Solomon Right.
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:

# My Solution:
# prompt = input("Add a new member: ")
# with open("members.txt", "a") as f:
#    f.write(prompt)

# Course Solution:
# member = input("Add a new member: ")
# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()
# existing_members.append(member + "\n")
# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()


# Open your computer IDE and place the following in a Python file:
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# Then, create a program that:
# 1. generates multiple text files by iterating over the filenames list,
# 2. and writes the text Hello  inside each generated text file.

# My Solution:
# filenames = ['doc.txt',
#              'report.txt',
#              'presentation.txt']
# contents = ['hello',
#             'hello',
#             'hello']
# for content, filename in zip(contents, filenames):
#     file = open(f"files/{filename}", 'w')
#     file.write(content)

# Course Solution:
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()


# Please download the three text files a.txt, b.txt, and c.txt
# from the resources and place them in your computer IDE.
# Then, create a program that:
# 1. reads each text file and
# 2. prints out the content of each file in the command line.

# Solution:
# filenames = ['files/a.txt', 'files/b.txt', 'files/c.txt']
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)