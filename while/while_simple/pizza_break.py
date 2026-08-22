pizzas="\nPlease enter what you want take in pizza:"
pizzas += "\n(Enter 'quit' will stop it.)"
message=""
while True:
    message=input(pizzas)
    if message == 'quit':
        break
    else: 
        print(f"Add {message} in pizza.")

age="Please enter your age:"
message=""
while True:
    message=int(input(age))
    if message < 3:
        print("You are free.")
    elif message < 12:
        print("You need pay 10 dollar.")
    else:
        print("You need pay 15 dollar.")