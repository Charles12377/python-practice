pizzas="\nPlease enter what you want take in pizza:"
pizzas += "\n(Enter 'quit' will stop it.)"
message=""
while True:
    message=input(pizzas)
    if message == 'quit':
        break
    else: 
        print(f"Add {message} in pizza.")

