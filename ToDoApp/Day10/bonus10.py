try:
    length = float(input("What is the length? "))
    width = float(input("What is the width? "))

    if width == length:
        exit("That looks like a square.")
    #     ^prints in red since the text is inside exit()

    area = width * length
    print(area)

except ValueError:
    print("Please enter a number.")

