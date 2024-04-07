# form_1040.py
"""
Contains class for Form 1040
Class handles calculations for tax returns

Format for W-2 form dictionaries
dict_w2 = {"WAGES_TIPS_OTHER_COMP": 0000, "FEDERAL_INCOME_TAX_WITHHELD": 0000,
           "SOCIAL_SECURITY_WAGES": 0000, "SOCIAL_SECURITY_TAX_WITHHELD": 0000,
           "MEDICARE_WAGES_AND_TIPS": 0000, "MEDICARE_TAX_WITHHELD": 0000,
           "DEPENDANT_CARE_BENEFITS": 0000,
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
                 "FED_TAX_WITHHELD": 0000}
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
    medicaid_waiver_payments = 00.00  # 1d
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
    total_income = 00.00  # 9, Total of lines 1z, 2b-6b, 7, and 8
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
    total_other_payments = 00.00  # 32, add lines 27 to 31
    total_payments = 00.00  # 33, add lines 25d, 26, and 32
    # REFUND / ADDITIONAL OWED
    # If line 33 is more than line 24
    overpaid = 00.00  # 34, subtract line 24 from 33
    default_overpaid = 00.00
    # If line 33 is less than line 24
    amount_owed = 00.00  # 37, subtract line 33 from 24
    default_owed = 00.00

    # Form W2 and 1099 Calculation Variables
    forms_w2 = list()
    form_1099_div = list()
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
            form_1099_div = list()
        self.forms_w2 = forms_w2
        self.form_1099_div = form_1099_div

    def total_forms_w2(self):
        """Total income and taxes from Form(s) W2"""
        total_income = 00.00
        total_withheld = 00.00

        # Loop through list of forms
        for form in self.forms_w2:
            total_income += form["WAGES_TIPS_OTHER_COMP"]
            total_withheld += form["FEDERAL_INCOME_TAX_WITHHELD"]

        # Assign total values to appropriate locations
        self.income_w2 = total_income
        self.tax_withheld_w2 = total_withheld

    def total_forms_1099(self):
        """Total income and taxes from Form(s) 1099"""
        tax_withheld_1099 = 0.00

        # Total tax withheld from all states
        for form in self.form_1099_div:
            tax_withheld_1099 += form["FED_TAX_WITHHELD"]

        self.tax_withheld_1099 = tax_withheld_1099

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
        if filing_status == "Single":
            self.filing_status = 0
        elif filing_status == "Married Filing Jointly":
            self.filing_status = 1
        elif filing_status == "Married Filing Separately":
            self.filing_status = 2
        elif filing_status == "Head of Household":
            self.filing_status = 3
        elif filing_status == "Qualifying Surviving Spouse":
            self.filing_status = 4

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

    # INCOME
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
        self.medicaid_waiver_payments = dollars

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
                               self.medicaid_waiver_payments + self.dependent_care_benefits +
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
        SEE IRS 1040 INSTRUCTIONS PAGE 34 FOR MORE INFORMATION

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
        if self.is_dependent or self.spouse_is_dependent == True:  # If the user or their spouse can be claimed
            checks = 0
            if self.user_age >= 65:
                checks += 1
            if self.user_is_blind:
                checks += 1
            if self.spouse_age >= 65:
                checks += 1
            if self.spouse_is_blind:
                checks += 1

            if self.total_income <= 850:  # If the users earned income is less than $850
                total = 1250
            else:  # If the users earned income is greater than $850
                total = self.total_income + 400
                if self.filing_status == 0 or self.filing_status == 2:  # If filing status is single or married filing separately
                    if total < 13850:
                        pass  # Do nothing
                    else:
                        total = 13850
                elif self.filing_status == 1:  # If filing status is married filing jointly
                    if total < 27700:
                        pass  # Do nothing
                    else:
                        total = 27700
                else:  # If filing status is head of household
                    if total < 20800:
                        pass  # Do nothing
                    else:
                        total = 20800

            if self.user_age < 65 and not self.user_is_blind and self.spouse_age < 65 and not self.spouse_is_blind:  # If the user and spouse are under 65 and not blind
                self.standard_deduction = total
            else:  # If the user or spouse are over 65 or blind
                if self.filing_status == 0 or self.filing_status == 3:  # If filing status is single of head of house
                    self.standard_deduction = 1850 * checks + total
                else:
                    self.standard_deduction = 1500 * checks + total
        else:  # If the user AND their spouse cannot be claimed as dependents
            checks = 0
            if self.user_age >= 65:
                checks += 1
            if self.user_is_blind:
                checks += 1
            if self.spouse_age >= 65:
                checks += 1
            if self.spouse_is_blind:
                checks += 1

            if checks > 0:  # For seniors or the blind
                if self.filing_status == 0:  # If filing status is single
                    if checks == 1:
                        self.standard_deduction = 15700
                    else:
                        self.standard_deduction = 17550
                elif self.filing_status == 1:  # If filing status is married filing jointly
                    if checks == 1:
                        self.standard_deduction = 29200
                    elif checks == 2:
                        self.standard_deduction = 30700
                    elif checks == 3:
                        self.standard_deduction = 32200
                    else:
                        self.standard_deduction = 33700
                elif self.filing_status == 2:  # If filing status is married filing separately
                    if checks == 1:
                        self.standard_deduction = 15350
                    elif checks == 2:
                        self.standard_deduction = 16850
                    elif checks == 3:
                        self.standard_deduction = 18350
                    else:
                        self.standard_deduction = 19850
                elif self.filing_status == 3:  # If filing status is head of household
                    if checks == 1:
                        self.standard_deduction = 22650
                    else:
                        self.standard_deduction = 24500
                else:  # If filing status is qualifying surviving spouse
                    if checks == 1:
                        self.standard_deduction = 29200
                    else:
                        self.standard_deduction = 30700
            else:  # For anyone under 65 AND NOT blind
                if self.filing_status == 0:  # Single
                    self.standard_deduction = 13850
                elif self.filing_status == 1:  # Married Filing Jointly
                    self.standard_deduction = 27700
                elif self.filing_status == 2:  # Married Filing Separately
                    self.standard_deduction = 13850
                elif self.filing_status == 3:  # Head of Household
                    self.standard_deduction = 20800
                else:  # Qualifying Surviving Spouse
                    self.standard_deduction = 27700

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

    # TAXES AND CREDITS
    def set_tax(self, dollars):
        """
        Mutator for tax

        :param dollars: taxes from various forms
        :return: N/A
        """
        self.tax = dollars

    def set_amount_schedule_2(self, dollars):
        """
        Mutator for amount_schedule_2

        :param dollars: value from schedule 2 line 3
        :return: N/A
        """
        self.amount_schedule_2 = dollars

    def calc_total_16_17(self):
        """
        Calculate total of lines 16 and 17 for line 18 value

        :return: N/A
        """
        self.total_16_17 = self.tax + self.amount_schedule_2

    def set_child_tax_credit(self, dollars):
        """
        Mutator for child_tax_credit

        :param dollars: value of child tax credits in dollars
        :return: N/A
        """
        self.child_tax_credit = dollars

    def set_amount_schedule_3_line_8(self, dollars):
        """
        Mutator for amount_schedule_3_line_8

        :param dollars: value of line 20 in dollars
        :return: N/A
        """
        self.amount_schedule_3_line_8 = dollars

    def calc_total_19_20(self):
        """
        Calculate the total of lines 19 and 20 for line 21

        :return: N/A
        """
        self.total_19_20 = self.child_tax_credit + self.amount_schedule_3_line_8

    def calc_sub_21_18(self):
        """
        Calculate difference between lines 21 and 18 for line 22
        If zero or less, set to zero

        :return: N/A
        """
        self.subtract_21_from_18 = self.total_16_17 - self.total_19_20
        if self.subtract_21_from_18 <= 0:
            self.subtract_21_from_18 = 0

    def set_other_taxes(self, dollars):
        """
        Mutator for other_taxes

        :param dollars: Value of other taxes in dollars
        :return: N/A
        """
        self.other_taxes = dollars

    def calc_total_tax(self):
        """
        Calculate total taxes by adding the totals from lines 22 and 23

        :return: N/A
        """
        self.total_tax = self.subtract_21_from_18 + self.other_taxes

    # PAYMENTS
    def set_tax_withheld_w2(self, dollars):
        """
        Mutator for tax_withheld_w2

        :param dollars: value of taxes withheld in dollars
        :return: N/A
        """
        self.tax_withheld_w2 = dollars

    def set_tax_withheld_1099(self, dollars):
        """
        Mutator for tax_withheld_1099

        :param dollars: value of taxes withheld in dollars
        :return: N/A
        """
        self.tax_withheld_1099 = dollars

    def set_tax_withheld_other(self, dollars):
        """
        Mutator for tax_withheld_other

        :param dollars: value of taxes withheld in dollars
        :return: N/A
        """
        self.tax_withheld_other = dollars

    def calc_total_withheld(self):
        """
        Calculate total taxes withheld

        :return: N/A
        """
        self.total_withheld = self.tax_withheld_w2 + self.tax_withheld_1099 + self.tax_withheld_other

    def set_estimate_tax_payments(self, dollars):
        """
        Mutator for estimate_tax_payments

        :param dollars: value of estimate in dollars
        :return: N/A
        """
        self.estimate_tax_payments = dollars

    def set_earned_income_credit(self, dollars):
        """
        Mutator for earned_income_credit

        :param dollars: value of earned income credit in dollars
        :return: N/A
        """
        self.earned_income_credit = dollars

    def set_additional_child_tax_credit(self, dollars):
        """
        Mutator for additional_child_tax_credit

        :param dollars: value of additional child tax credit in dollars
        :return: N/A
        """
        self.additional_child_tax_credit = dollars

    def set_american_opportunity_credit(self, dollars):
        """
        Mutator for american_opportunity_credit

        :param dollars: value of american opportunity credit in dollars
        :return: N/A
        """
        self.american_opportunity_credit = dollars

    def set_amount_schedule_3_line_15(self, dollars):
        """
        Mutator for amount_schedule_3_line_15

        :param dollars: value of line 31 in dollars
        :return: N/A
        """
        self.amount_schedule_3_line_15 = dollars

    def calc_total_other_payments(self):
        """
        Calculate total_other_payments by adding up lines 27 to 30

        :return: N/A
        """
        self.total_other_payments = (self.earned_income_credit + self.additional_child_tax_credit +
                                     self.american_opportunity_credit + self.amount_schedule_3_line_15)

    def calc_total_payments(self):
        """
        Calculate total_payments using values from lines 25d, 26, and 32

        :return: N/A
        """
        self.total_payments = self.total_other_payments + self.total_withheld + self.estimate_tax_payments

    # REFUND/AMOUNT OWED
    def calc_refund(self):
        """
        Determine if the user receives a refund or owes additional taxes
        Calculate the value of the refund or amount owed

        :return: N/A
        """
        # If total_payments is greater than total_tax, the user receives a refund
        if self.total_payments > self.total_tax:
            self.overpaid = self.total_payments - self.total_tax
            self.amount_owed = 00.00
        # If total_payments is less than total_tax, the user owes additional taxes
        elif self.total_payments < self.total_tax:
            self.amount_owed = self.total_tax - self.total_payments
            self.overpaid = 00.00
        # If they are equal, the user neither owes money nor receives a refund
        else:
            self.overpaid = 0
            self.amount_owed = 0

    # ACCESSORS
    def get_filing_status(self):
        """
        Accessor for filing_status
        0 == Single
        1 == Married Filing Jointly
        2 == Married Filing Separately
        3 == Head of Household
        4 == Qualifying Surviving Spouse

        :return: String Value for Filing Status
        """
        if self.filing_status == 0:
            status = "Single"
        elif self.filing_status == 1:
            status = "Married Filing Jointly"
        elif self.filing_status == 2:
            status = "Married Filing Separately"
        elif self.filing_status == 3:
            status = "Head of Household"
        elif self.filing_status == 4:
            status = "Qualifying Surviving Spouse"

        return status

    def get_has_digital_assets(self):
        """
        Accessor for has_digital_assets

        :return: Boolean value
        """
        return self.has_digital_assets

    def get_is_dependent(self):
        """
        Accessor for is_dependent

        :return: Boolean value
        """
        return self.is_dependent

    def get_spouse_is_dependent(self):
        """
        Accessor for spouse_is_dependent

        :return: Boolean value
        """
        return self.spouse_is_dependent

    def get_spouse_itemizes_separately(self):
        """
        Accessor for spouse_itemizes_separately

        :return: Boolean value
        """
        return self.spouse_itemizes_separately

    def get_is_dual_status_alien(self):
        """
        Accessor for is_dual_status_alien

        :return: Boolean value
        """
        return self.is_dual_status_alien

    def get_user_age(self):
        """
        Accessor for user_age

        :return: Integer for user_age
        """
        return self.user_age

    def get_user_is_blind(self):
        """
        Accessor for user_is_blind

        :return: Boolean value
        """
        return self.user_is_blind

    def get_spouse_age(self):
        """
        Accessor for spouse_age

        :return: Integer for spouse_age
        """
        return self.spouse_age

    def get_spouse_is_blind(self):
        """
        Accessor for spouse_is_blind

        :return: Boolean value
        """
        return self.spouse_is_blind

    def get_dependents(self):
        """
        Accessor for dependents

        :return: List of dependents
        """
        return self.dependents

    def get_income_w2(self):
        """
        Accessor for income_w2

        :return: Float value
        """
        return self.income_w2

    def get_household_employee_wages(self):
        """
        Accessor for household_employee_wages

        :return: Float value
        """
        return self.household_employee_wages

    def get_tip_income(self):
        """
        Accessor for tip_income

        :return: Float value
        """

    def get_medicaid_waiver_payments(self):
        """
        Accessor for medicaid_waiver_payments

        :return: Float value
        """
        return self.medicaid_waiver_payments

    def get_dependent_care_benefits(self):
        """
        Accessor for dependent_care_benefits

        :return: Float value
        """
        return self.dependent_care_benefits

    def get_employer_adoption_benefits(self):
        """
        Accessor for employer_adoption_benefits

        :return: Float value
        """
        return self.employer_adoption_benefits

    def get_wages_form_8919(self):
        """
        Accessor for wages_form_8919

        :return: Float value
        """
        return self.wages_form_8919

    def get_other_income(self):
        """
        Accessor for other_income

        :return: Float value
        """
        return self.other_income

    def get_combat_pay(self):
        """
        Accessor for combat_pay

        :return: Float value
        """
        return self.combat_pay

    def get_total_1a_to_1h(self):
        """
        Accessor for total_1a_to_1h

        :return: Float value
        """
        return self.total_1a_to_1h

    def get_tax_exempt_interest(self):
        """
        Accessor for tax_exempt_interest

        :return: Float value
        """
        return self.tax_exempt_interest

    def get_taxable_interest(self):
        """
        Accessor for taxable_interest

        :return: Float value
        """
        return self.taxable_interest

    def get_qualified_dividends(self):
        """
        Accessor for qualified_dividends

        :return: Float value
        """
        return self.qualified_dividends

    def get_ordinary_dividends(self):
        """
        Accessor for ordinary_dividends

        :return: Float value
        """
        return self.ordinary_dividends

    def get_ira_distributions(self):
        """
        Accessor for ira_distributions

        :return: Float value
        """
        return self.ira_distributions

    def get_ira_taxable(self):
        """
        Accessor for ira_taxable

        :return: Float value
        """
        return self.ira_taxable

    def get_pensions_annuities(self):
        """
        Accessor for pensions_annuities

        :return: Float value
        """
        return self.pensions_annuities

    def get_pensions_annuities_taxable(self):
        """
        Accessor for pensions_annuities_taxable

        :return: Float value
        """
        return self.pensions_annuities_taxable

    def get_social_security_benefits(self):
        """
        Accessor for social_security_benefits

        :return: Float value
        """
        return self.social_security_benefits

    def get_ss_benefits_taxable(self):
        """
        Accessor for ss_benefits_taxable

        :return: Float value
        """
        return self.ss_benefits_taxable

    def get_use_lump_sum(self):
        """
        Accessor for lump_sum

        :return: Boolean value
        """
        return self.use_lump_sum

    def get_capital_gain_or_loss(self):
        """
        Accessor for capital_gain_or_loss

        :return: Float value
        """
        return self.capital_gain_or_loss

    def get_income_schedule_1(self):
        """
        Accessor for income_schedule_1

        :return: Float value
        """
        return self.income_schedule_1

    def get_total_income(self):
        """
        Accessor for total_income

        :return: Float value
        """
        return self.total_income

    def get_adjustments(self):
        """
        Accessor for adjustments

        :return: Float value
        """
        return self.adjustments

    def get_adjusted_gross_income(self):
        """
        Accessor for adjusted_gross_income

        :return: Float value
        """
        return self.adjusted_gross_income

    def get_standard_deduction(self):
        """
        Accessor for standard_deduction

        :return: Float value
        """
        return self.standard_deduction

    def get_qualified_business_income_deduction(self):
        """
        Accessor for qualified_business_income_deduction

        :return: Float value
        """
        return self.qualified_business_income_deduction

    def get_total_deductions(self):
        """
        Accessor for total_deductions

        :return: Float value
        """
        return self.total_deductions

    def get_taxable_income(self):
        """
        Accessor for taxable_income

        :return: Float value
        """
        return self.taxable_income

    def get_tax(self):
        """
        Accessor for tax

        :return: Float value
        """
        return self.tax

    def get_amount_schedule_2(self):
        """
        Accessor for amount_schedule_2

        :return: Float value
        """
        return self.amount_schedule_2

    def get_total_16_17(self):
        """
        Accessor for total_16_17

        :return: Float value
        """
        return self.total_16_17

    def get_child_tax_credit(self):
        """
        Accessor for child_tax_credit

        :return: Float value
        """
        return self.child_tax_credit

    def get_amount_schedule_3_line_18(self):
        """
        Accessor for amount_schedule_3_line_18

        :return: Float value
        """
        return self.amount_schedule_3_line_8

    def get_total_19_20(self):
        """
        Accessor for total_19_20

        :return: Float value
        """
        return self.total_19_20

    def get_subtract_21_from_18(self):
        """
        Accessor for subtract_21_from_18

        :return: Float value
        """
        return self.subtract_21_from_18

    def get_other_taxes(self):
        """
        Accessor for other_taxes

        :return: Float value
        """
        return self.other_taxes

    def get_total_tax(self):
        """
        Accessor for total_tax

        :return: Float value
        """
        return self.total_tax

    def get_tax_withheld_w2(self):
        """
        Accessor for tax_withheld_w2

        :return: Float value
        """
        return self.tax_withheld_w2

    def get_tax_withheld_1099(self):
        """
        Accessor for tax_withheld_1099

        :return: Float value
        """
        return self.tax_withheld_1099

    def get_tax_withheld_other(self):
        """
        Accessor for tax_withheld_other

        :return: Float value
        """
        return self.tax_withheld_other

    def get_total_withheld(self):
        """
        Accessor for total_withheld

        :return: Float value
        """
        return self.total_withheld

    def get_estimate_tax_payments(self):
        """
        Accessor for estimate_tax_payments

        :return: Float value
        """
        return self.estimate_tax_payments

    def get_earned_income_credit(self):
        """
        Accessor for earned_income_credit

        :return: Float value
        """
        return self.earned_income_credit

    def get_additional_child_tax_credit(self):
        """
        Accessor for additional_child_tax_credit

        :return: Float value
        """
        return self.additional_child_tax_credit

    def get_american_opportunity_credit(self):
        """
        Accessor for american_opportunity_credit

        :return: Float value
        """
        return self.american_opportunity_credit

    def get_amount_schedule_3_line_15(self):
        """
        Accessor for amount_schedule_3_line_15

        :return: Float value
        """
        return self.amount_schedule_3_line_15

    def get_total_other_payments(self):
        """
        Accessor for total_other_payments

        :return: Float value
        """
        return self.total_other_payments

    def get_total_payments(self):
        """
        Accessor for total_payments

        :return: Float value
        """
        return self.total_payments

    def get_overpaid(self):
        """
        Accessor for overpaid

        :return: Float value
        """
        return self.overpaid

    def get_amount_owed(self):
        """
        Accessor for amount_owed

        :return: Float value
        """
        return self.amount_owed

    def get_forms_w2(self):
        """
        Accessor for forms_w2

        :return: List of W2 forms
        """
        return self.forms_w2

    def get_form_1099_div(self):
        """
        Accessor for form_1099_div

        :return: Dictionary 1099-DIV
        """
        return self.form_1099_div

    def add_w2(self, form):
        """
        Function to append a new W2 form to the end of the list of W2 forms

        :param form: W2 form as a dictionary
        :return: N/A
        """
        self.forms_w2.append(form)
        self.total_forms_w2()

    def add_ten_99(self, form):
        """
        Function to append a new W2 form to the end of the list of W2 forms

        :param form: W2 form as a dictionary
        :return: N/A
        """
        self.form_1099_div.append(form)
        self.total_forms_1099()

    def calc_all(self):
        """
        Run or rerun all calculation functions

        :return: N/A
        """
        self.total_forms_w2()
        self.total_forms_1099()
        self.total_lines_1a_to_1h()
        self.calc_total_income()
        self.calc_adjusted_gross_income()
        self.calc_standard_deduction()
        self.calc_total_deductions()
        self.calc_taxable_income()
        self.calc_total_16_17()
        self.calc_total_19_20()
        self.calc_sub_21_18()
        self.calc_total_tax()
        self.calc_total_withheld()
        self.calc_total_other_payments()
        self.calc_total_payments()
        self.calc_refund()
