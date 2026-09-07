class Resteurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def describe_restaurant(self):
        print(f"{self.name} provide {self.type}.")

    def open_restaurant(self):
        print(f"The {self.name} is open.")

restaurant=Resteurant('兰州牛肉面','noodles')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()