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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
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

        if value <= 0:
            raise ValueError("Invalid input, must enter a positive number.")

        return value

    def validate_other_states(self, other_states):
        """
        Validate the Income Tax from other states.
        Calls validate_other_states_tax for each state in the list

        :param other_states: List of other states
        :return: Validate list of other states
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
    
