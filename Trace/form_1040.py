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
    filing_status = 0
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
    total_deductions = 00.00  # 14, add lines 12 and 13
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

    def __init__(self, forms_w2=None, form_1099_div=None, other_income_1099=0, other_tax_1099=0):
        """
        Constructor

        :param forms_w2: list of w2 forms in dictionary format
        :param form_1099_div: form 1099-DIV in dictionary format
        :param other_income_1099: income from other 1099 forms
        :param other_tax_1099: taxes withheld from other 1099 forms
        """
        if forms_w2 is None:
            forms_w2 = list()
        if form_1099_div is None:
            form_1099_div = dict()
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

    def set_filing_status(self, filing_status):
        """
        Mutator for filing_status
        0 == Single
        1 == Married Filing Jointly
        2 == Married Filing Separately
        3 == Head of Household
        4 == Qualifying Surviving Spouse

        :param filing_status: string value representing the user's filing status
        :return: N/A
        """
        pass

    def set_has_digital_assets(self, has_digital_assets):
        """
        Mutator for has_digital_assets

        :param has_digital_assets: boolean
        :return: N/A
        """
        self.has_digital_assets = has_digital_assets

    def set_is_dependent(self, is_dependent):
        """
        Mutator for is_dependent

        :param is_dependent: boolean, can someone else claim the user as a dependent
        :return: N/A
        """
        self.is_dependent = is_dependent

    def set_spouse_is_dependent(self, spouse_is_dependent):
        """
        Mutator for spouse_is_dependant

        :param spouse_is_dependent: boolean, can someone else claim the user's spouse as a dependent
        :return: N/A
        """
        self.spouse_is_dependent = spouse_is_dependent

    def set_spouse_itemizes_separately(self, spouse_itemizes_separately):
        """
        Mutator for spouse_itemizes_separately

        :param spouse_itemizes_separately: boolean, does the user's spouse itemize on a different return
        :return: N/A
        """
        self.spouse_itemizes_separately = spouse_itemizes_separately

    def set_is_dual_status_alien(self, is_dual_status_alien):
        """
        Mutator for is_dual_status_alien

        :param is_dual_status_alien: boolean, is the user a dual status alien
        :return: N/A
        """
        self.is_dual_status_alien = is_dual_status_alien

    def set_user_age(self, age):
        """
        Mutator for user_age

        :param age: Age of the user
        :return: N/A
        """
        self.user_age = age

    def set_user_is_blind(self, is_blind):
        """
        Mutator for user_is_blind

        :param is_blind: boolean, is the user blind
        :return: N/A
        """
        self.user_is_blind = is_blind

    def set_spouse_age(self, age):
        """
        Mutator for spouse_age

        :param age: Age of the user's spouse
        :return: N/A
        """
        self.spouse_age = age

    def set_spouse_is_blind(self, is_blind):
        """
        Mutator for spouse_is_blind

        :param is_blind: boolean, is the user's spouse blind
        :return: N/A
        """
        self.spouse_is_blind = is_blind

    def set_dependents(self, dependents):
        """
        Mutator for dependents

        :param dependents: list of dependents
        :return: N/A
        """
        self.dependents = dependents

    def set_income_w2(self, dollars):
        """
        Mutator for income_w2

        :param dollars: Total income from all W-2 Forms
        :return: N/A
        """
        self.income_w2 = dollars

    def set_household_employee_wages(self, dollars):
        """
        Mutator for household_employee_wages

        :param dollars: household employee wages not reported on Form W-2
        :return: N/A
        """
        self.household_employee_wages = dollars

    def set_tip_income(self, dollars):
        """
        Mutator for tip_income

        :param dollars: Tip income not reported on Form W-2
        :return: N/A
        """
        self.tip_income = dollars

    def set_medicaid_waiver_payments(self, dollars):
        """
        Mutator for medicaid_waiver_payments

        :param dollars: Medicaid waiver payments not reported on Form W-2
        :return: N/A
        """
        self.medicaid_wavier_payments = dollars

    def set_dependent_care_benefits(self, dollars):
        """
        Mutator for dependent_care_benefits

        :param dollars: Taxable dependent care benefits from Form 2441, line 26
        :return: N/A
        """
        self.dependent_care_benefits = dollars

    def set_employer_adoption_benefits(self, dollars):
        """
        Mutator for employer_adoption_benefits

        :param dollars: Employer adoption benefits from Form 8839, line 29
        :return: N/A
        """
        self.employer_adoption_benefits = dollars

    def set_wages_form_8919(self, dollars):
        """
        Mutator for wages_form_8919

        :param dollars: Wages from Form 8919, line 6
        :return: N/A
        """
        self.wages_form_8919 = dollars

    def set_other_income(self, dollars):
        """
        Mutator for other_income

        :param dollars: Other earned income not reported
        :return: N/A
        """
        self.other_income = dollars

    def total_lines_1a_to_1h(self):
        """
        Adds up total value for line 1a to 1h, provides value for line 1z

        :return: N/A
        """
        self.total_1a_to_1h = (self.income_w2 + self.household_employee_wages + self.tip_income +
                               self.medicaid_wavier_payments + self.dependent_care_benefits +
                               self.employer_adoption_benefits + self.wages_form_8919 + self.other_income)

    def set_tax_exempt_interest(self, dollars):
        """
        Mutator for tax_exempt_interest

        :param dollars: Tax-exempt interest
        :return: N/A
        """
        self.tax_exempt_interest = dollars

    def set_taxable_interest(self, dollars):
        """
        Mutator for taxable_interest

        :param dollars: Taxable interest
        :return: N/A
        """
        self.taxable_interest = dollars

    def set_qualified_dividends(self, dollars):
        """
        Mutator for qualified_dividends

        :param dollars: Qualified dividends
        :return: N/A
        """
        self.qualified_dividends = dollars

    def set_ordinary_dividends(self, dollars):
        """
        Mutator for ordinary_dividends

        :param dollars: Ordinary dividends
        :return: N/A
        """
        self.ordinary_dividends = dollars

    def set_ira_distributions(self, dollars):
        """
        Mutator for ira_distributions

        :param dollars: IRA distributions
        :return: N/A
        """
        self.ira_distributions = dollars

    def set_ira_taxable(self, dollars):
        """
        Mutator for ira_taxable

        :param dollars: Taxable amount from IRA Distributions
        :return: N/A
        """
        self.ira_taxable = dollars

    def set_pensions_annuities(self, dollars):
        """
        Mutator for pensions_annuities

        :param dollars: Pensions and annuities
        :return: N/A
        """
        self.pensions_annuities = dollars

    def set_pensions_annuities_taxable(self, dollars):
        """
        Mutator for pensions_annuities_taxable

        :param dollars: Taxable amount from pensions and annuities
        :return: N/A
        """
        self.pensions_annuities_taxable = dollars

    def set_social_security_benefits(self, dollars):
        """
        Mutator for social_security_benefits

        :param dollars: Social Security Benefits
        :return: N/A
        """
        self.social_security_benefits = dollars

    def set_ss_benefits_taxable(self, dollars):
        """
        Mutator for ss_benefits_taxable

        :param dollars: Taxable amount from social security benefits
        :return: N/A
        """
        self.ss_benefits_taxable = dollars

    def set_use_lump_sum(self, truefalse):
        """
        Mutator for use_lump_sum

        :param truefalse: Boolean, if the user elects to use the lump-sum election method
        :return: N/A
        """
        self.use_lump_sum = truefalse

    def set_capital_gain_or_loss(self, dollars):
        """
        Mutator for capital_gain_or_loss

        :param dollars: Capital gain or loss
        :return: N/A
        """
        self.capital_gain_or_loss = dollars

    def set_income_schedule_1(self, dollars):
        """
        Mutator for income_schedule_1

        :param dollars: Additional income from schedule 1, line 26
        :return: N/A
        """
        self.income_schedule_1 = dollars

    def calc_total_income(self):
        """
        Calculate total income using values from line 1z, 2b-6b, 7 and 8 for line 9

        :return: N/A
        """
        self.total_income = (self.total_1a_to_1h + self.taxable_interest + self.ordinary_dividends +
                             self.ira_taxable + self.pensions_annuities_taxable + self.ss_benefits_taxable +
                             self.capital_gain_or_loss + self.income_schedule_1)

    def set_adjustments(self, dollars):
        """
        Mutator for adjustments

        :param dollars: Adjustments to income from schedule 1, line 26
        :return: N/A
        """
        self.adjustments = dollars

    def calc_adjusted_gross_income(self):
        """
        Calculate adjusted gross income using values from line 9 and 10

        :return: N/A
        """
        self.adjusted_gross_income = self.total_income - self.adjustments

    def calc_standard_deduction(self):
        """
        Determine the user's standard deduction value
        Required fields:
            Filing Status
            Age
            Blindness
            Spouse Age (if any)
            Spouse Blindness (if any)
            User or spouse is a dependent
            If spouse itemizes on a separate return or the user is a dual-status alien

        :return: N/A
        """
        pass

    def set_qualified_business_income_deduction(self, dollars):
        """
        Mutator for qualified_business_income_deduction

        :param dollars: Qualified income deduction from Form 8995 or 8995-A
        :return: N/A
        """
        self.qualified_business_income_deduction = dollars

    def calc_total_deductions(self):
        """
        Calculate total deductions using values from lines 12 and 13

        :return: N/A
        """
        self.total_deductions = self.standard_deduction + self.qualified_business_income_deduction

    def calc_taxable_income(self):
        """
        Calculate total taxable income
        Subtract line 14 from 11, if zero or less, then default to zero

        :return: N/A
        """
        self.taxable_income = self.adjusted_gross_income - self.total_deductions

        # If taxable_income is 0 or less, set to 0
        if self.taxable_income <= 0:
            self.taxable_income = 0




