todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()
    # ^allows for entries with whitespace to make it to match block

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
        # case 'show' | 'display':
            # ^bitwise OR operator |
            for item in todos:
                # item = item.title()
                print(item)
        case 'exit':
            break
        # case _:
        #     # ^convention to use underscore for unknown variables
        #     print("Hey, you entered an unknown command")

print("Bye!")

