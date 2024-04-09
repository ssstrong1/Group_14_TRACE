# input_validation.py
"""
Contains functions for validating user input.
Will require a separate validator function for each user input entry.
"""


class FormValidatorW2:
    """
    Class dedicated to validating W-2 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """
    def validate_wages_tips_other_comp(self, dollars: str) -> float:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_federal_income_tax_withheld(self, dollars: str) -> float:
        """
        Validate the Federal Income Tax Withheld from form W-2

        :param dollars: Federal Income Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_social_security_wages(self, dollars: str) -> float:
        """
        Validate the Social Security Wages from form W-2

        :param dollars: Social Security Wages from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_social_security_tax(self, dollars: str) -> float:
        """
        Validate the Social Security Tax from form W-2

        :param dollars: Social Security Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_medicare_wages(self, dollars: str) -> float:
        """
        Validate the Medicare Wages from form W-2

        :param dollars: Medicare Wages from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_medicare_tax(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_dependant_care_benefits(self, dollars: str) -> float:
        """
        Validate the Dependant Care Benefits from form W-2

        :param dollars: Dependant Care Benefits from form W-2
        :return: Validated benefits value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_state_wages_tips(self, dollars: str) -> float:
        """
        Validate the State Wages, Tips, Etc. from form W-2

        :param dollars: State Wages, Tips, Etc. from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_state_income_tax(self, dollars: str) -> float:
        """
        Validate the State Income Tax from form W-2

        :param dollars: State Income Tax from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_local_income(self, dollars: str) -> float:
        """
        Validate the Local Wages, Tips, Etc. from form W-2

        :param dollars: Local Wages, Tips, Etc. from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_local_income_tax(self, dollars: str) -> float:
        """
        Validate the Local Income Tax from form W-2

        :param dollars: Local Income Tax from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_other_states(self, other_states):
        """
        Validate the Income and Income Tax from other states.
        Uses validate_state_wages_tips() and validate_state_income_tax()
        :param other_states: List of other states
        :return: Validate list of other states
        :raises ValueError: Functions called will raise a ValueError with an
        appropriate message.
        """
        for state in other_states:
            try:
                state["STATE_INCOME"] = self.validate_local_income(state["STATE_INCOME"])
                state["STATE_TAX_WITHHELD"] = self.validate_local_income_tax(state["STATE_TAX_WITHHELD"])
            except ValueError:
                raise ValueError("Invalid input, must enter a positive number.")


class FormValidator1099DIV:
    """
    Class dedicated to validating 1099 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """
    def validate_ordinary_dividends(self, dollars: str) -> float:
        """
        Validate the Total Ordinary Dividends from form 1099-DIV

        :param dollars: Total Ordinary Dividends from form 1099-DIV
        :return: Validated dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_qualified_dividends(self, dollars: str) -> float:
        """
        Validate the Qualified Dividends from form 1099-DIV

        :param dollars: Qualified Dividends from form 1099-DIV
        :return: Validate dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_capital_gain_distr(self, dollars: str) -> float:
        """
        Validate the Total Capital Gain Distribution from form 1099-DIV

        :param dollars: Total Capital Gain Distribution from form 1099-DIV
        :return: Validated gains value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_unrecap_sec_1250_gain(self, dollars: str) -> float:
        """
        Validate the Unrecaptured Sections 1250 Gains from form 1099-DIV

        :param dollars: Unrecaptured Sections 1250 Gains from form 1099-DIV
        :return: Validate gains value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_section_1202_gain(self, dollars: str) -> float:
        """
        Validate the Section 1202 Gains from form 1099-DIV

        :param dollars: Section 1202 Gains from form 1099-DIV
        :return: Validated gains value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_collectibles_gain(self, dollars: str) -> float:
        """
        Validate the Collectibles (28%) Gain from form 1099-DIV

        :param dollars: Collectibles (28%) Gain from form 1099-DIV
        :return: Validated gains value as string
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_section_897_ordinary_dividends(self, dollars: str) -> float:
        """
        Validate the Section 897 Ordinary Dividends from form 1099-DIV

        :param dollars: Section 897 Ordinary Dividends from form 1099-DIV
        :return: Validated dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_section_897_capital_gain(self, dollars: str) -> float:
        """
        Validate the Section 897 Capital Gain from form 1099-DIV

        :param dollars: Section 897 Capital Gain
        :return: Validated gains value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_nondividend_distributions(self, dollars: str) -> float:
        """
        Validate Nondividend Distributions from form 1099-DIV

        :param dollars: Nondividend Distributions from form 1099-DIV
        :return: Validated distributions value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_income_tax_withheld(self, dollars: str) -> float:
        """
        Validate Federal Income Tax Withheld from form 1099-DIV

        :param dollars: Federal Income Tax Withheld from form 1099-DIV
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_section_199a_dividends(self, dollars: str) -> float:
        """
        Validate Section 199A Dividends from form 1099-DIV

        :param dollars: Section 199A Dividends from form 1099-DIV
        :return: Validated dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_investment_expenses(self, dollars: str) -> float:
        """
        Validate Investment Expenses from form 1099-DIV

        :param dollars: Investment Expenses from form 1099-DIV
        :return: Validated expenses value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_foreign_tax_paid(self, dollars: str) -> float:
        """
        Validate Foreign Tax Paid from form 1099-DIV

        :param dollars: Foreign Tax Paid from form 1099-DIV
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_foreign_country_or_us_possession(self, dollars: str) -> float:
        """
        Validate Foreign Country or US Possession from form 1099-DIV

        :param dollars: Country or US Possession from form 1099-DIV
        :return: Validated country value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_cash_liquidation_distributions(self, dollars: str) -> float:
        """
        Validate Cash Liquidation Distributions from form 1099-DIV

        :param dollars: Cash Liquidation Distributions from form 1099-DIV
        :return: Validated distributions value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_noncash_liquidation_distributions(self, dollars: str) -> float:
        """
        Validate Noncash Liquidation Distributions from form 1099-DIV

        :param dollars: Noncash Liquidation Distributions from form 1099-DIV
        :return: Validated distributions value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_exempt_interest_dividends(self, dollars: str) -> float:
        """
        Validate Exempt Interest Dividends from form 1099-DIV

        :param dollars: Exempt Interest Dividends from form 1099-DIV
        :return: Validate dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_private_activity_bond_interest_dividends(self, dollars: str) -> float:
        """
        Validate Specified Private Activity Bond Interest Dividends from form 1099-DIV

        :param dollars: Specified Private Activity Bond Interest Dividends from form 1099-DIV
        :return: Validate dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_other_states_tax(self, dollars: str) -> float:
        """
        Validate State Tax Withheld
        FUNCTION USED FOR validate_other_states

        :param dollars: State Tax Withheld
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, must enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_other_states(self, other_states):
        """
        Validate the Income Tax from other states.
        Calls validate_other_states_tax for each state in the list

        :param other_states: List of other states
        :return: Validated list of other states
        :raises ValueError: Functions called will raise a ValueError with an
        appropriate message.
        """
        for state in other_states:
            try:
                state["STATE_TAX_WITHHELD"] = self.validate_other_states_tax(state["STATE_TAX_WITHHELD"])
            except ValueError:
                raise ValueError("Invalid input, must enter a positive number.")


class FormValidator1040:
    """
    Class dedicated to validating 1040 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """

    def validate_filing_status(self, status: str):
        """
        Validate filing_status from form 1040

        :param status: filing_status string
        :return: Validated status value as string
        :raises ValueError: If validation fails, with an appropriate error message
        """
        status_list = ["Single", "Married Filing Jointly", "Married Filing Separately",
                       "Head of Household", "Qualifying Surviving Spouse"]
        if status in status_list:
            return status
        else:
            raise ValueError("Invalid input, must select a valid filing status.")

    def validate_user_age(self, age: str) -> int:
        """
        Validate user_age from form 1040

        :param age: Age integer from form 1040
        :return: Validated age value as int
        :raises ValueError:
        """
        try:
            value = int(age)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive integer")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive integer")

        return value

    def validate_spouse_age(self, age: str) -> int:
        """
        Validate spouse_age from form 1040

        :param age: Spouse age integer from form 1040
        :return: Validate age value as int
        """
        try:
            value = int(age)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive integer")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive integer")

        return value

    def validate_income_w2(self, dollars: str) -> float:
        """
        Validate income_w2 from form 1040

        :param dollars: Form W2 income from form 1040 line 1a
        :return: Validate income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_household_employee_income(self, dollars: str) -> float:
        """
        Validate household_employee_income from form 1040

        :param dollars: household employee income from form 1040 line 1b
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_tip_income(self, dollars: str) -> float:
        """
        Validate tip_income from form 1040

        :param dollars: tip income from form 1040 line 1c
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_medicaid_waiver_payments(self, dollars: str) -> float:
        """
        Validate medicaid_waiver_payments from form 1040

        :param dollars: medicaid waiver payments from form 1040 line 1d
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_dependent_care_benefits(self, dollars: str) -> float:
        """
        Validate dependent_care_benefits from form 1040

        :param dollars: dependent care benefits from form 1040 line 1e
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_employer_adoption_benefits(self, dollars: str) -> float:
        """
        Validate employer_adoption_benefits from form 1040

        :param dollars: employer_adoption_benefits from form 1040 line 1f
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_wages_form_8919(self, dollars: str) -> float:
        """
        Validate wages_form_8919 from form 1040

        :param dollars: wages form 8919 from form 1040 line 1g
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_other_income(self, dollars: str) -> float:
        """
        Validate other_income from form 1040

        :param dollars: other income from form 1040 line 1h
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_combat_pay(self, dollars: str) -> float:
        """
        Validate combat_pay from form 1040

        :param dollars: combat pay from form 1040 line 1i
        :return: Validated income value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_tax_exempt_interest(self, dollars: str) -> float:
        """
        Validate tax_exempt_interest from form 1040

        :param dollars: tax exempt interest from form 1040 line 2a
        :return: Validated interest value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_taxable_interest(self, dollars: str) -> float:
        """
        Validate taxable_interest from form 1040

        :param dollars: taxable interest from form 1040 line 2b
        :return: Validated interest value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_qualified_dividends(self, dollars: str) -> float:
        """
        Validate qualified_dividends from form 1040

        :param dollars: qualified dividends from form 1040 line 3a
        :return: Validated dividends value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_ordinary_dividends(self, dollars: str) -> float:
        """
        Validate ordinary_dividends from form 1040

        :param dollars: ordinary dividends from form 1040 line 3b
        :return: Validated dividends value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_ira_distributions(self, dollars: str) -> float:
        """
        Validate ira_distributions from form 1040

        :param dollars: ira distributions from form 1040 line 4a
        :return: Validated distributions value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_ira_taxable(self, dollars: str) -> float:
        """
        Validate ira_taxable from form 1040

        :param dollars: ira taxable from form 1040 line 4b
        :return: Validated distributions value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_pensions_annuities(self, dollars: str) -> float:
        """
        Validate pensions_annuities from form 1040

        :param dollars: pension annuities from form 1040 line 5a
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_pensions_annuities_taxable(self, dollars: str) -> float:
        """
        Validate pensions_annuities_taxable from form 1040

        :param dollars: pensions annuities taxable from form 1040 line 5b
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_social_security_benefits(self, dollars: str) -> float:
        """
        Validate social_security_benefits from form 1040

        :param dollars: social security benefits from form 1040 line 6a
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_ss_benefits_taxable(self, dollars: str) -> float:
        """
        Validate ss_benefits_taxable from form 1040

        :param dollars: ss benefits from form 1040 line 6b
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_capital_gain_or_loss(self, dollars: str) -> float:
        """
        Validate capital_gain_or_loss from form 1040

        :param dollars: capital gain or loss from form 1040 line 7
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_income_schedule_1(self, dollars: str) -> float:
        """
        Validate income_schedule_1 from form 1040

        :param dollars: income schedule 1 from form 1040 line 8
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_adjustments(self, dollars: str) -> float:
        """
        Validate adjustments from form 1040

        :param dollars: adjustments to income from form 1040 line 10
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_qualified_business_income_deduction(self, dollars: str) -> float:
        """
        Validate qualified_business_income_deduction from form 1040

        :param dollars: qualified business income deduction from form 1040 line 13
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_tax(self, dollars: str) -> float:
        """
        Validate tax from form 1040

        :param dollars: tax from form 1040 line 16
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_amount_schedule_2(self, dollars: str) -> float:
        """
        Validate amount_schedule_2 from form 1040

        :param dollars: amount from schedule 2 from form 1040 line 17
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_child_tax_credit(self, dollars: str) -> float:
        """
        Validate child_tax_credit from form 1040

        :param dollars: child tax credit from form 1040 line 19
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_amount_schedule_3_line_8(self, dollars: str) -> float:
        """
        Validate amount_schedule_3_line_8 from form 1040

        :param dollars: amount from schedule 3 line 8 from form 1040 line 20
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_other_taxes(self, dollars: str) -> float:
        """
        Validate other_taxes from form 1040

        :param dollars: other taxes from form 1040 line 23
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_tax_withheld_w2(self, dollars: str) -> float:
        """
        Validate tax_withheld_w2 from form 1040

        :param dollars: tax withheld from form w2 from form 1040 line 25a
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_tax_withheld_1099(self, dollars: str) -> float:
        """
        Validate tax_withheld_1099 from form 1040

        :param dollars: tax withheld from form 1099 from form 1040 line 25b
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_tax_withheld_other(self, dollars: str) -> float:
        """
        Validate tax_withheld_other from form 1040

        :param dollars: tax withheld other from form 1040 line 25c
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_estimate_tax_payments(self, dollars: str) -> float:
        """
        Validate estimate_tax_payments from form 1040

        :param dollars: estimate tax payments from form 1040 line 26
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_earned_income_credit(self, dollars: str) -> float:
        """
        Validate earned_income_credit from form 1040

        :param dollars: earned_income_credit from form 1040 line 27
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_additional_child_tax_credit(self, dollars: str) -> float:
        """
        Validate additional_child_tax_credit from form 1040

        :param dollars: additional child tax credit from form 1040 line 28
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_american_opportunity_credit(self, dollars: str) -> float:
        """
        Validate american_opportunity_credit from form 1040

        :param dollars: american opportunity credit from form 1040 line 29
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value

    def validate_amount_schedule_3_line_15(self, dollars: str) -> float:
        """
        Validate amount_schedule_3_line_15 from form 1040

        :param dollars: amount from schedule 3 line 15 from form 1040 line 30
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            raise ValueError("Invalid input, please enter a positive number.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive number")

        return value




    
