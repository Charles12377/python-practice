class User:
    def __init__(self,f_name,l_name,gender,school):
        self.f_name=f_name
        self.l_name=l_name
        self.gender=gender
        self.school=school
        self.number=0

    def describe_user(self):
        print(f"{self.f_name}{self.l_name} {self.gender} {self.school}")

    def greet_user(self):
        print(f"Hello {self.f_name}{self.l_name},welcome come to here.")

    def increment_login_attempts(self,new_user=1):
        self.number += new_user

    def reset_attempts(self,number=0):
        self.number=number