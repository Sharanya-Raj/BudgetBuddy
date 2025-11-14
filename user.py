import csv
class User:
    def email_or_username_exists(self, email, userName):
        opened_file = open('users.csv', mode = "r")
        for row in opened_file:
            user_data = row.split(',')
            return [
                user_data[0] == self.userName,
                user_data[2] == self.email
            ]

    def valid_password(self, password):
        return (self, len(password) >= 8 and any(char.isdigit() for char in password)
                and any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and any(char in '!@#$%^&*()-_+=' for char in password))

    def initUser(self, userName, password, email, studentNJIT):
        self.userName = userName
        self.password = password
        self.email = email
        self.studentNJIT = studentNJIT
        self.income = []
        self.expenses = []
        return self
    
    def login(self, inputUserName, inputPassword):
        return self.userName == inputUserName and self.password == inputPassword