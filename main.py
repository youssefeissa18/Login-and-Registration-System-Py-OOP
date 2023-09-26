import re
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

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

class UserManage:
    def __init__(self):
        self.Users = []

    @staticmethod
    def is_valid_email(email):
        # Use a simple regular expression to validate email
        return re.match(r'^[\w\.-]+@[\w\.-]+$', email) is not None

    def  RegisterUser(self):
        while True:
            name = input("Enter Your Name : ")
            age = int(input("Enter Your Age : "))
            email = input("Enter Your Email : ")
            password = input("Enter Your Password : ")
            if len(password) >= 8 and UserManage.is_valid_email(email):
                new_User = User(name, email, password, age)
                self.Users.append(new_User)
                print("Your Registration User Do Successfully")
                break
            else:
                print("Your Info do You Enter is Valid and Try Again")

    def login_User(self, email, password):
        for UserIndex in self.Users:
            if UserIndex.get_email() == email and password == UserIndex.get_password():
                print("You Login Successfully")
                return True
        else:
            print("You Password Or Email Wrong Try Again")
            return False

    def Show_User_List(self):
        print("User List:")
        for UserIndex in self.Users:
            # print("Name: " + UserIndex.get_name())
            print(f"NAME : {UserIndex.get_name()}\t\tAGE : {UserIndex.get_age()}")


print("============================== Login and Registration System ==============================")
user = UserManage()
while True:
    print("1. Register User\n2. Login User\n3. Show User List\n4. Search User\n5. Delete User\n6. Exit")
    choice = int(input("Enter Your Choice "))
    if  choice == 1:
        user.RegisterUser()
    elif choice == 2:
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")
        user.login_User(email, password)
    elif choice == 3:
        user.Show_User_List()
    elif choice == 6:
        print("============================== Login and Registration System Terminate ==============================")
        exit(0)



