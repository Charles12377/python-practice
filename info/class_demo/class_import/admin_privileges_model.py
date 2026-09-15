from user_model import User
class Privileges:
    def __init__(self,privileges):
        self.privileges=privileges

    def show_privileges(self):
        print(f"Admin can {self.privileges}.")

class Admin(User):
    def __init__(self, f_name, l_name, gender, school,privileges):
        super().__init__(f_name, l_name, gender, school)
        self.privileges=Privileges(privileges)