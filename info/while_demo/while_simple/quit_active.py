pizzas="\nPlease enter what you want take in pizza:"
pizzas += "\n(Enter 'quit' will stop it.)"
active=True
while active:
    message=input(pizzas)
    if message == 'quit':
        active=False
    else:
        print(f"Add {message}.")