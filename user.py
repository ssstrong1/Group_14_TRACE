import sqlite3

class User():
    def __init__(self, id, fisrt_name, last_name, email, password):
        self.id = id
        self.first_name = fisrt_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_to_db(self):
        connection = sqlite3.connect('tax_calculator.db')
        cursor = connection.cursor()

        cursor.execute(''' INSERT INTO Users (id, first_name, last_name, email, password) 
        VALUES (?, ?, ?, ?, ?) ''', (self.id, self.first_name, self.last_name, self.email, self.password))

        connection.commit()
        connection.close()


if __name__ == "__main__":
    id = int(input("Enter your ID: "))
    fisrt_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Enter password: ")

    new_user = User(id, fisrt_name, last_name,email,password)
    new_user.save_to_db()

    print("User added")



