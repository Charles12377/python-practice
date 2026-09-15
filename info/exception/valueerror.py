print("Enter two numbers to add.")

while True:
    try:
        f_number=int(input("first number:"))
        l_number=int(input("last number:"))
        print(f_number+l_number)
    except ValueError:
        pass


