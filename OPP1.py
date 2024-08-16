class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def get_info(self):
        return (f"Foydalanuvchi: {self.name}, "
                f"ismi: {self.username}, "
                f"email: {self.email}")

user1 = User('Dima_1301', 'Dilmurod', 'Dima_1301@gmail.com')
print(user1.get_info())



