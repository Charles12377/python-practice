pizzas="\nPlease enter what you want take in pizza:"
pizzas += "\n(Enter 'quit' will stop it.)"
message=""
while message!='quit':
    message=input(pizzas)
    if message != 'quit':
        print(f"Add {message}.")
        
    
    