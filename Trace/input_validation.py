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
    def validate_wages_tips_other_comp(self, wages: str) -> float:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param wages: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_federal_income_tax_withheld(self, tax: str) -> float:
        """
        Validate the Federal Income Tax Withheld from form W-2

        :param tax: Federal Income Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_social_security_wages(self, wages: str) -> float:
        """
        Validate the Social Security Wages from form W-2

        :param wages: Social Security Wages from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_social_security_tax(self, tax: str) -> float:
        """
        Validate the Social Security Tax from form W-2

        :param tax: Social Security Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_medicare_wages(self, wages: str) -> float:
        """
        Validate the Medicare Wages from form W-2

        :param wages: Medicare Wages from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_medicare_tax(self, tax: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param tax: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_dependant_care_benefits(self, benefits: str) -> float:
        """
        Validate the Dependant Care Benefits from form W-2

        :param benefits: Dependant Care Benefits from form W-2
        :return: Validated benefits value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_state_wages_tips(self, wages: str) -> float:
        """
        Validate the State Wages, Tips, Etc. from form W-2

        :param wages: State Wages, Tips, Etc. from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_state_income_tax(self, tax: str) -> float:
        """
        Validate the State Income Tax from form W-2

        :param tax: State Income Tax from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_local_wages_tips(self, wages: str) -> float:
        """
        Validate the Local Wages, Tips, Etc. from form W-2

        :param wages: Local Wages, Tips, Etc. from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_local_income_tax(self, tax: str) -> float:
        """
        Validate the Local Income Tax from form W-2

        :param tax: Local Income Tax from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_other_states(self, other_states):
        """
        Validate the Income and Income Tax from other states.
        Uses validate_state_wages_tips() and validate_state_income_tax()
        :param other_states: List of other states
        :return: Validate list of other states
        :raises ValueError: Functions called will raise a ValueError with an
        appropriate message.
        """
        pass


class FormValidator1099DIV:
    """
    Class dedicated to validating W-2 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """
    def validate_ordinary_dividends(self, dividends: str) -> float:
        """
        Validate the Total Ordinary Dividends from form 1099-DIV

        :param dividends: Total Ordinary Dividends from form 1099-DIV
        :return: Validated dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_qualified_dividends(self, dividends: str) -> float:
        """
        Validate the Qualified Dividends from form 1099-DIV

        :param dividends: Qualified Dividends from form 1099-DIV
        :return: Validate dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_capital_gain_distr(self, gains: str) -> float:
        """
        Validate the Total Capital Gain Distribution from form 1099-DIV

        :param gains: Total Capital Gain Distribution from form 1099-DIV
        :return: Validated gains value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_unrecap_sec_1250_gain(self, gains: str) -> float:
        """
        Validate the Unrecaptured Sections 1250 Gains from form 1099-DIV

        :param gains: Unrecaptured Sections 1250 Gains from form 1099-DIV
        :return: Validate gains value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_section_1202_gain(self, gains: str) -> float:
        """
        Validate the Section 1202 Gains from form 1099-DIV

        :param gains: Section 1202 Gains from form 1099-DIV
        :return: Validated gains value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_collectibles_gain(self, gains: str) -> float:
        """
        Validate the Collectibles (28%) Gain from form 1099-DIV

        :param gains: Collectibles (28%) Gain from form 1099-DIV
        :return: Validated gains value as string
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_section_897_ordinary_dividends(self, dividends: str) -> float:
        """
        Validate the Section 897 Ordinary Dividends from form 1099-DIV

        :param dividends: Section 897 Ordinary Dividends from form 1099-DIV
        :return: Validated dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_section_897_capital_gain(self, gains: str) -> float:
        """
        Validate the Section 897 Capital Gain from form 1099-DIV

        :param gains: Section 897 Capital Gain
        :return: Validated gains value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_nondividend_distributions(self, distributions: str) -> float:
        """
        Validate Nondividend Distributions from form 1099-DIV

        :param distributions: Nondividend Distributions from form 1099-DIV
        :return: Validated distributions value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_income_tax_withheld(self, tax: str) -> float:
        """
        Validate Federal Income Tax Withheld from form 1099-DIV

        :param tax: Federal Income Tax Withheld from form 1099-DIV
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_section_199a_dividends(self, dividends: str) -> float:
        """
        Validate Section 199A Dividends from form 1099-DIV

        :param dividends: Section 199A Dividends from form 1099-DIV
        :return: Validated dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_investment_expenses(self, expenses: str) -> float:
        """
        Validate Investment Expenses from form 1099-DIV

        :param expenses: Investment Expenses from form 1099-DIV
        :return: Validated expenses value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_foreign_tax_paid(self, tax: str) -> float:
        """
        Validate Foreign Tax Paid from form 1099-DIV

        :param tax: Foreign Tax Paid from form 1099-DIV
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_foreign_country_or_us_possession(self, country: str) -> float:
        """
        Validate Foreign Country or US Possession from form 1099-DIV

        :param country: Country or US Possession from form 1099-DIV
        :return: Validated country value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_cash_liquidation_distributions(self, distributions: str) -> float:
        """
        Validate Cash Liquidation Distributions from form 1099-DIV

        :param distributions: Cash Liquidation Distributions from form 1099-DIV
        :return: Validated distributions value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_noncash_liquidation_distributions(self, distributions: str) -> float:
        """
        Validate Noncash Liquidation Distributions from form 1099-DIV

        :param distributions: Noncash Liquidation Distributions from form 1099-DIV
        :return: Validated distributions value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_exempt_interest_dividends(self, dividends: str) -> float:
        """
        Validate Exempt Interest Dividends from form 1099-DIV

        :param dividends: Exempt Interest Dividends from form 1099-DIV
        :return: Validate dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_private_activity_bond_interest_dividends(self, dividends: str) -> float:
        """
        Validate Specified Private Activity Bond Interest Dividends from form 1099-DIV

        :param dividends: Specified Private Activity Bond Interest Dividends from form 1099-DIV
        :return: Validate dividends value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """
        pass

    def validate_other_states_tax(self, tax: str) -> float:
        """
        Validate State Tax Withheld
        FUNCTION USED FOR validate_other_states

        :param tax: State Tax Withheld
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message
        """

    def validate_other_states(self, other_states):
        """
        Validate the Income Tax from other states.
        Calls validate_other_states_tax for each state in the list

        :param other_states: List of other states
        :return: Validate list of other states
        :raises ValueError: Functions called will raise a ValueError with an
        appropriate message.
        """
        pass
