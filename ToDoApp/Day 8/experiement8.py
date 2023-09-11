with open("files/doc.txt") as file:
    # open assigns read, so it doesn't need second argument "r"
    print("HI")
file.read()
# this doesn't print since it's not in indented with block,
# cuz with block closes file

