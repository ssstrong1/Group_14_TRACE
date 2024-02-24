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


class FormValidator1099:
    """
    Class dedicated to validating 1099 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """
    
