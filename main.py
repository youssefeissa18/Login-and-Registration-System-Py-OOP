class User:
    def __init__(self, name, password, email, age):
        self.name = name
        self.password = password
        self.email = email
        self.age = age

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

class UserManage:
    def __init__(self):
        self.Users = []

    def  RegisterUser(self, name, password, email, age):
        name = input("Enter Your Name : ")
        password = input("Enter Your Password : ")
        email = input("Enter Your Email : ")
        age = int(input("Enter Your Age : "))
        new_User = User(name, password,email,age)
        self.Users.append(new_User)
        print("Your Registration User Do Successfully")
    


print("============================== Login and Registration System ==============================")
print("1. Register User\n2. Login User\n3. Show User List\n4. Search User\n5. Delete User")