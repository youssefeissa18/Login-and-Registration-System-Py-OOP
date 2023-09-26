class User:
    def __init__(self,  name, email, password, age):
        self.name = name
        self.password = password
        self.email = email
        self.age = age

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_Email(self):
        return self.email

class UserManage:
    def __init__(self):
        self.Users = []

    def  RegisterUser(self):
        name = input("Enter Your Name : ")
        age = int(input("Enter Your Age : "))
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")
        new_User = User(name, email, password, age)
        self.Users.append(new_User)
        print("Your Registration User Do Successfully")

    def login_User(self, email, password):
        for UserIndex in self.Users:
            if UserIndex.get_Email() == email and password == UserIndex.get_password():
                print("You Login Successfully")
                return True
        else:
            print("You Password Or Email Wrong Try Again")
            return False


print("============================== Login and Registration System ==============================")
print("1. Register User\n2. Login User\n3. Show User List\n4. Search User\n5. Delete User")
user = UserManage()
while True:
    choice = int(input("Enter Your Choice "))
    if  choice == 1:
        user.RegisterUser()
    elif choice == 2:
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")
        user.login_User(email, password)
    
