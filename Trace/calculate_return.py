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
           "STATE_INCOME":
           [{"STATE": "STATE01", "STATE_INCOME": 0000, "STATE_TAX_WITHHELD": 0000},
            {"STATE": "STATE02", "STATE_INCOME": 0000, "STATE_TAX_WITHHELD": 0000}]}

Format for 1099 form dictionaries
dict_1099 = {"RENT": 0000,
             "ROYALTIES": 0000,
             "OTHER_INCOME": 0000, "FEDERAL_INCOME_TAX_WITHHELD": 0000,
             "FISHING_BOAT_PROCEEDS": 0000, "MEDICAL_AND_HEALTH_CARE_PAYMENTS": 0000,
             "DIRECT_SALES": False, "SUBSTITUTE_PAYMENTS": 0000,
             "CROP_INSURANCE": 0000, "GROSS_PROCEEDS_TO_ATTORNEY": 0000,
             "FISH_FOR_RESALE": 0000, "409A_DEFERRALS": 0000,
             "EXCESS_GOLDEN_PARACHUTE": 0000, "DEFERRED_COMPENSATION": 0000,
             "STATE_INCOME":
             [{"STATE": "STATE01", "STATE_TAX_WITHHELD": 0000, "STATE_INCOME": 0000},
              {"STATE": "STATE02", "STATE_TAX_WITHHELD": 0000, "STATE_INCOME": 0000}]}
"""


def calculate_state_return(forms_w2, forms_1099, other_income, filing_status, is_dependant, user_age, spouse_age=0, is_blind=False, spouse_is_blind=False):
    """
    :param forms_w2: list composed of dictionary objects that represent W-2 forms
    :param forms_1099: list composed of dictionary objects that represent 1099 forms
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

    Function to calculate state tax returns.
    """
    STANDARD_DEDUCTION = [13850, 13850, 27700, 20800, 27700]
    STANDARD_DEDUCTION_SENIOR =
    total_income_w2 = 0             # total amount of income from form(s) W-2, box 1 (Wages, tips, other compensation)
    total_tax_w2 = 0                # total taxes paid from form(s) W-2
    total_income_1099 = 0           # total amount of income from form(s) 1099
    total_tax_1099 = 0              # total taxes paid from form(s) 1099
    total_income = 0                # total taxable income from all sources
    total_tax = 0                   # total taxes paid from all sources
    adjusted_gross_income = 0       # total taxable income after adjustments from schedule 1

    for form in forms_w2:
        # Loop through list of W-2 forms and total up any required values
        break

    for form in forms_1099:
        # Loop through list of 1099 forms and total up any required values
        break

    pass
