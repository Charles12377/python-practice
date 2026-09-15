class Restaurant:
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

class IceCreamstand(Restaurant):
    def __init__(self,name,type,*flavors):
        super().__init__(name,type)
        self.flavors=flavors

    def descripe_ice(self):
        print(f"My favourate icecream is {self.flavors}.")

icecream=IceCreamstand('puddy','ice','老冰棍','小布丁','甜筒')
icecream.descripe_ice()    