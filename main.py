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




print("============================== Login and Registration System ==============================")
print("1. Register User\n2. Login User\n3. Show User List\n4. Search User\n5. Delete User")