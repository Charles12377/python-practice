class Resteurant:
    def __init__(self,name,type,):
        self.name=name
        self.type=type
        self.number_save=0

    def describe_restaurant(self):
        print(f"{self.name} provide {self.type}.")

    def open_restaurant(self):
        print(f"The {self.name} is open.")

    def set_number_saved(self,new_number_save):
        if self.number_save<=new_number_save:
            self.number_save=new_number_save
        else:
            print("Please enter anothor number.")

    def increment_number_saved(self,increment_number):
        self.number_save += increment_number

restaurant=Resteurant('兰州牛肉面','noodles')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_1=Resteurant('古丽花儿','xingjiang foods')
restaurant_1.describe_restaurant()
restaurant.number_save=5
print(restaurant.number_save)
restaurant.set_number_saved(8)
print(restaurant.number_save)
restaurant.increment_number_saved(5)
print(restaurant.number_save)