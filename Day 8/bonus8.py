date = input("Enter the date: ")
mood = input("Enter your mood 1-10: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"files/journal/{date}.txt", "w") as file:
    file.write("Mood is: " + mood + 2 * '\n')
    file.write("Thoughts are: " + thoughts)
