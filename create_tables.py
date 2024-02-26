import sqlite3

connection = sqlite3.connect('tax_calculator.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS TaxDoc (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        tax_year INTEGER,
        annual_income REAL,
        deductions REAL,
        taxable_income REAL,
        tax_credits REAL,
        doc TEXT,
        state TEXT,
        zipcode INTEGER,
        filing_status TEXT,
        date_created TEXT,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    )
''')
connection.commit()
connection.close()