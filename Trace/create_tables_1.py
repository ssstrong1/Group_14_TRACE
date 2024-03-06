import sqlite3

# connect to or creates sqlite db
user_connection = sqlite3.connect('tax_calculator.db')

# cursor obj to execute queries
user_cursor = user_connection.cursor()

# creating users table
user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL, 
        password TEXT NOT NULL
    )
''')

# creating the tax calc table
user_cursor.execute('''
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
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# commit
user_connection.commit()

