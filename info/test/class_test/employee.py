"""包含姓名，薪资的类"""
class Employee():
    def __init__(self,f_name,l_name,salary):
        self.name=f"{f_name} {l_name}"
        self.salary=salary

    def give_raise(self,salary_raise=500000):
        self.salary += salary_raise

    