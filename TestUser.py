import sqlite3
from datetime import datetime

connection = sqlite3.connect('tax_calculator.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO Users(first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
               ('John', 'Doe', 'jdoe@email.com', 'password123'))
connection.commit()

cursor.execute("SELECT id FROM Users WHERE first_name = 'John' AND last_name = 'Doe' ")
user_id = cursor.fetchone()[0]

cursor.execute("INSERT INTO TaxDoc(user_id, tax_year, annual_income, deductions, taxable_income,"
               "tax_credits, doc, state, zipcode, filing_status, date_created) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
               (user_id, 2024, 60000.00, 5000.00, 55000.00, 2000.00, 'W-2', 'NC',
                27545, 'Single', str(datetime.now())))
connection.commit()

cursor.execute("SELECT * FROM Users JOIN tax_calculator ON Users.id = tax_calculator.user_id")
result = cursor.fetchall()

for row in result:
    print(row)

connection.close()