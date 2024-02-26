import sqlite3
from datetime import datetime


class TaxDoc():
    def __init__(self, id, user_id, tax_year, annual_income, deductions, taxable_income,
                 tax_credits, doc, state, zipcode, filing_status, date_created):
        self.id = id
        self.user_id = user_id
        self.tax_year = tax_year
        self.annual_income = annual_income
        self.deductions = deductions
        self.taxable_income = taxable_income
        self.tax_credits = tax_credits
        self.doc = doc
        self.state = state
        self.zipcode = zipcode
        self.filing_status = filing_status
        self.date_created = date_created

    def save_to_db(self):
        connection = sqlite3.connect('tax_calculator.db')
        cursor = connection.cursor()

        cursor.execute(''' INSERT INTO TaxDoc (id, user_id, tax_year, annual_income, deductions, 
        taxable_income, tax_credits, doc, state, zipcode, filing_status, date_created)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?)''',
                       (self.id, self.user_id, self.tax_year, self.annual_income, self.deductions,
                        self.taxable_income, self.tax_credits, self.doc, self.state, self.zipcode,
                        self.filing_status, self.date_created))

        connection.commit()
        connection.close()


if __name__ == "__main__":
    id = input("Enter ID: ")
    user_id = input("Enter User ID: ")
    tax_year = input("Enter tax year: ")
    annual_income = input("Enter annual income: ")
    deductions = input("Enter deductions: ")
    taxable_income = input("Enter taxable income: ")
    tax_credits = input("Enter tax credits: ")
    doc = input("Enter document type: ")
    state = input("Enter the state you are filing in: ")
    zipcode = input("Enter zipcode: ")
    filing_status = input("Enter filing status: ")
    date_created = datetime.now()
    print(date_created)

    new_tax_doc = TaxDoc(id, user_id, tax_year, annual_income, deductions, taxable_income, tax_credits, doc, state,
                         zipcode, filing_status, date_created)
    new_tax_doc.save_to_db()

    print("Tax document successully added. ")
