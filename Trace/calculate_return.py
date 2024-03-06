# calculate_return.py
"""
Contains function(s) for calculating and returning the user's tax returns based on user input as parameters.

Format for W-2 form dictionaries
dict_w2 = {"WAGES_TIPS_OTHER_COMP": 0000, "FEDERAL_INCOME_TAX_WITHHELD": 0000,
           "SOCIAL_SECURITY_WAGES": 0000, "SOCIAL_SECURITY_TAX_WITHHELD": 0000,
           "MEDICARE_WAGES_AND_TIPS": 0000, "MEDICARE_TAX_WITHHELD": 0000,
           "DEPENDANT_CARE_BENEFITS": 0000,
           "STATE_WAGES_TIPS_ETC": 0000, "STATE_INCOME_TAX": 0000,
           "LOCAL_WAGES_TIPS_ETC": 0000, "LOCAL_INCOME_TAX": 0000,
           "STATES":
           [{"STATE": "STATE01", "STATE_INCOME": 0000, "STATE_TAX_WITHHELD": 0000},
            {"STATE": "STATE02", "STATE_INCOME": 0000, "STATE_TAX_WITHHELD": 0000}]}

Format for 1099 DIV form dictionaries
dict_1099_div = {"ORDINARY_DIVIDENDS": 0000,
                 "QUALIFIED_DIVIDENDS": 0000,
                 "CAPITAL_GAIN_DISTR": 0000, "UNRECAP_SEC_1250_GAIN": 0000,
                 "SECTION_1202_GAIN": 0000, "COLLECTIBLES_GAIN": 0000,
                 "SECTION_897_ORDINARY_DIVIDENDS": 0000, "SECTION_897_CAPITAL_GAIN": 0000,
                 "NONDIVIDEND_DISTRIBUTIONS": 0000, "INCOME_TAX_WITHHELD": 0000,
                 "SECTION_1999A_DIVIDENDS": 0000, "INVESTMENT_EXPENSES": 0000,
                 "FOREIGN_TAX_PAID": 0000, "FOREIGN_COUNTRY_OR_US_POSSESSION": "Country",
                 "CASH_LIQUIDATION_DISTRIBUTIONS": 0000, "NONCASH_LIQUIDATION_DISTRIBUTIONS": 0000,
                 "EXEMPT_INTEREST_DIVIDENDS": 0000, "PRIVATE_ACTIVITY_BOND_INTEREST_DIVIDENDS": 0000,
                 "STATES":
                 [{"STATE": "STATE01", "STATE_TAX_WITHHELD": 0000},
                  {"STATE": "STATE02", "STATE_TAX_WITHHELD": 0000}]}
"""


def total_form_w2(forms_w2):
    """
    Function to total up taxable income and taxes withheld from all W-2 forms

    :param forms_w2: List of W-2 forms in dictionary format
    :return: total_income, total_taxes
    """
    for form in forms_w2:
        # Loop through list of W-2 forms and total up any required values
        break
    pass


def total_form_1099_div(form_1099_div):
    """
    Function to total up taxable income and taxes withheld from 1099-DIV form

    :param form_1099_div: 1099-DIV form in dictionary format
    :return: total_income, total_taxes
    """
    pass


def calculate_1040(total_income_w2, total_taxes_w2, total_income_1099_div, total_taxes_1099_div, other_income, filing_status, is_dependant, user_age, spouse_age=0, is_blind=False, spouse_is_blind=False):
    """
    Function to calculate tax returns based on information in 1040 form

    :param total_income_w2: Total income from form W-2
    :param total_taxes_w2: Total Taxes from form
    :param total_income_1099_div: Total income from form 1099-DIV
    :param total_taxes_1099_div: Total taxes from form 1099-DIV
    :param other_income: any other taxable income not recorded in forms W-2 and 1099
    :param filing_status: an integer 1-5 representing the user's filing status
        1 - Single
        2 - Married Filing Jointly
        3 - Married Filing Separately
        4 - Head of Household
        5 - Qualifying Surviving Spouse
    :param is_dependant: boolean, can someone else claim the user as a dependant
    :param user_age: age of the user
    :param spouse_age: age of the users spouse (Default value=0. If 0, assume no spouse)
    :param is_blind: boolean, is the user blind (Receive the same standard deduction as someone over 65)
    :param spouse_is_blind: boolean, is the user's spouse blind
    :return: value of refund or value of additional payment due
    """
    STANDARD_DEDUCTION = [13850, 13850, 27700, 20800, 27700]
    STANDARD_DEDUCTION_SENIOR = []
    STANDARD_DEDUCTION_SENIOR_AND_BLIND = []
    total_income = 0                # total taxable income from all sources
    total_tax = 0                   # total taxes paid from all sources
    adjusted_gross_income = 0       # total taxable income after adjustments from schedule 1
    pass
