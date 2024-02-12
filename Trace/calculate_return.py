#calculate_return.py
"""
Contains function(s) for calculating and returning the user's tax returns based on user input as parameters.
"""

def calculate_state_return(forms_w2, forms_1099):
    """
    :param forms_w2: list composed of dictionary objects that represent W-2 forms.
    :param forms_1099: list composed of dictionary objects that represent 1099 forms.
    :return: value of refund or value of additional taxes due.
    Function to calculate state tax returns.
    """
    total_income = 0    # total amount of income from form(s) W-2, box 1 (Wages, tips, other compensation)

    for form in forms_w2:
        # Loop through list of W-2 forms and total up any required values.
        break

    for form in forms_1099:
        # Loop through list of 1099 forms and total up any required values.
        break

    pass
