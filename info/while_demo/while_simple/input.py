message=input("What car do you like?")
print(f"Let me see if I can find you a {message}.")

number=input("How many people have food?")
number=int(number)
if number > 8:
    print("It is not enough table.")
else:
    print("Welcome!")

num=input("Please give me a number.")
num=int(num)
if num % 10 == 0:
    print("该数是10的倍数。")
