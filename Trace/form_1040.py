# form_1040.py
"""
Contains class for Form 1040
Class handles calculations for tax returns

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


class Form1040:
    """
    Class for Form 1040, handles tax return calculations


    """
    filing_status = ""
    has_digital_assets = False
    is_dependent = False
    spouse_is_dependent = False
    spouse_itemizes_separately = False
    is_dual_status_alien = False
    user_age = 00
    user_is_blind = False
    spouse_age = 00
    spouse_is_blind = False
    dependents = list()
    # INCOME
    income_w2 = 00.00  # 1a
    household_employee_wages = 00.00  # 1b
    tip_income = 00.00  # 1c
    medicaid_wavier_payments = 00.00  # 1d
    dependent_care_benefits = 00.00  # 1e
    employer_adoption_benefits = 00.00  # 1f
    wages_form_8919 = 00.00  # 1g
    other_income = 00.00  # 1h
    combat_pay = 00.00  # 1i
    total_1a_to_1h = 00.00  # 1z, Total of lines 1a to 1h
    tax_exempt_interest, taxable_interest = 00.00, 00.00  # 2a, 2b
    qualified_dividends, ordinary_dividends = 00.00, 00.00  # 3a, 3b
    ira_distributions, ira_taxable = 00.00, 00.00  # 4a, 4b
    pensions_annuities, pensions_annuities_taxable = 00.00, 00.00  # 5a, 5b
    social_security_benefits, ss_benefits_taxable = 00.00, 00.00  # 6a, 6b
    use_lump_sum = False  # 6c
    capital_gain_or_loss = 00.00  # 7
    income_schedule_1 = 00.00  # 8
    total_income = 00.00    # 9, Total of lines 1z, 2b-6b, 7, and 8
    adjustments = 00.00  # 10
    adjusted_gross_income = 00.00  # 11, subtract line 10 from line 9
    standard_deduction = 00.00  # 12
    qualified_business_income_deduction = 00.00  # 13
    total_12_and_13 = 00.00  # 14, add lines 12 and 13
    taxable_income = 00.00  # 15, subtract line 14 from 11, if zero or less == 00.00
    # TAX AND CREDITS
    tax = 00.00  # 16
    amount_schedule_2 = 00.00  # 17
    total_16_17 = 00.00  # 18, add lines 16 and 17
    child_tax_credit = 00.00  # 19
    amount_schedule_3_line_8 = 00.00  # 20
    total_19_20 = 00.00  # 21, add lines 19 and 20
    subtract_21_from_18 = 00.00  # 22, subtract line 21 from line 18, if zero or less == 00.00
    other_taxes = 00.00  # 23
    total_tax = 00.00  # 24, add lines 22 and 23
    # PAYMENTS
    tax_withheld_w2 = 00.00  # 25a
    tax_withheld_1099 = 00.00  # 25b
    tax_withheld_other = 00.00  # 25c
    total_withheld = 00.00  # 25d, total lines 25a to 25c
    estimate_tax_payments = 00.00  # 26
    earned_income_credit = 00.00  # 27
    additional_child_tax_credit = 00.00  # 28
    american_opportunity_credit = 00.00  # 29
    amount_schedule_3_line_15 = 00.00  # 30
    total_other_payments = 00.00  # 31, add lines 27 to 31
    total_payments = 00.00  # 32, add lines 25d, 26, and 32
    # REFUND / ADDITIONAL OWED
    # If line 33 is more than line 24
    overpaid = 00.00  # 34, subtract line 24 from 33
    # If line 33 is less than line 24
    amount_owed = 00.00  # 37, subtract line 33 from 24

    # Form W2 and 1099 Calculation Variables
    forms_w2 = list()
    form_1099_div = dict()
    form_1099_other_income = 00.00
    form_1099_other_taxes = 00.00

    def __init__(self, forms_w2, form_1099_div, other_income_1099, other_tax_1099):
        """
        Constructor

        :param forms_w2: list of w2 forms in dictionary format
        :param form_1099_div: form 1099-DIV in dictionary format
        :param other_income_1099: income from other 1099 forms
        :param other_tax_1099: taxes withheld from other 1099 forms
        """
        self.forms_w2 = forms_w2
        self.form_1099_div = form_1099_div

    def total_forms_w2(self):
        """Total income and taxes from Form(s) W2"""
        total_income = 00.00
        total_withheld = 00.00

        # Loop through list of forms
        for form in self.forms_w2:
            break
        pass

    def total_forms_1099(self):
        """Total income and taxes from Form(s) 1099"""
        total_income = 00.00
        total_withheld = 00.00

        total_income += self.form_1099_other_income
        total_withheld += self.form_1099_other_taxes
        pass



