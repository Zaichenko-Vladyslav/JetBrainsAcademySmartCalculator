# write your code here

import re  # to look for numbers in variable names (Invalid variable)

# Function that returns True if variable has digit \d in the name
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

while True:
    # Get user input for calculations
    user = input().strip()

    # Command ^ should be interpreted as ** (power):
    user = user.replace("^", "**")

    # If user input is empty, return nothing and continue
    if not user:
        continue

    # If user want to use command, that should start with "/"
    elif user[0] == "/":
        if user == "/exit":
            print("Bye!")
            break
        elif user == "/help":
            print("This program calculates the result of an expression with using variables")
            continue
        elif user.startswith('/'):
            print("Unknown command")
            continue
        else:
            pass
            continue

    # Program do not support command "//" and need to return ERROR message in this case
    elif "//" in user:
        print("Invalid assignment")
        continue

    # If user wants to initialize a new variable
    elif "=" in user:
        # If command "=" before the variable name, program need to return ERROR message
        if hasNumbers(user.split("=")[0]):
            print("Invalid identifier")
            continue
        try:
            # Built-in function "exec()" allow us to add new variabe
            exec(user)
            continue
        except:
            print("Invalid assignment")
            continue

    # If everything is okay, program should print result with using built-in function "eval()"
    try:
        print(int(eval(user)))
    except NameError:
        print("Unknown variable")
    except SyntaxError:
        print("Invalid expression")
