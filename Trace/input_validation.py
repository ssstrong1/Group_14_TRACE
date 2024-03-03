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
    Class dedicated to validating W-2 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """
    def validate_rent(self, rent: str) -> float:
        """
        Validate the Rent from form 1099

        :param rent: Rent from form 1099
        :return: Validated rent value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_royalties(self, royalties: str) -> float:
        """
        Validate the Royalties from form 1099

        :param royalties: Royalties from 1099
        :return: Validated royalties value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_other_income(self, income: str) -> float:
        """
        Validate the Other Income from form 1099

        :param income: Other Income from form 1099
        :return: Validated income value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_federal_income_tax_withheld(self, tax: str) -> float:
        """
        Validate the Federal Income Tax Withheld from form 1099

        :param tax: Federal Income Tax from form 1099
        :return: Validated tax value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_fishing_boat_proceeds(self, income: str) -> float:
        """
        Validate the Fishing Boat Proceeds from form 1099

        :param income: Fishing Boat Proceeds from form 1099
        :return: Validated income value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_medical_and_health_care_payments(self, payments: str) -> float:
        """
        Validate the Medical and Health Care Payments from form 1099

        :param payments: Medical and Health Care Payments from form 1099
        :return: Validated payments value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_substitute_payments(self, payments: str) -> float:
        """
        Validate the Substitute Payments from form 1099

        :param payments: Substitute Payments from form 1099
        :return: Validated payments value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_crop_insurance(self, proceeds: str) -> float:
        """
        Validate the Crop Insurance Proceeds from form 1099

        :param proceeds: Crop Insurance Proceeds from form 1099
        :return: Validated proceeds value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_gross_proceeds_to_attorney(self, proceeds: str) -> float:
        """
        Validate the Gross Proceeds Paid to an Attorney from form 1099

        :param proceeds: Gross Proceeds Paid to an Attorney from form 1099
        :return: Validate proceeds value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_fish_for_resale(self, payments: str) -> float:
        """
        Validate the Fish Purchased for Resale from form 1099

        :param payments: Value of Fish Purchased for Resale from form 1099
        :return: Validated payments value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_409a_deferrals(self, deferrals: str) -> float:
        """
        Validate the Section 409A Deferrals from form 1099

        :param deferrals: Value of Section 409A Deferrals from form 1099
        :return: Validated deferrals value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_excess_golden_parachute(self, payments: str) -> float:
        """
        Validate the Excess Golden Parachute Payments from form 1099

        :param payments: Excess Golden Parachute Payments from form 1099
        :return: Validated payments value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_deferred_compensation(self, comp: str) -> float:
        """
        Validate the Nonqualified Deferred Compensation from form 1099

        :param comp: Nonqualified Deferred Compensation from form 1099
        :return: Validated comp value as float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_state_income(self, income: str) -> float:
        """
        Validate the State Income from form 1099

        :param income: State Income
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_state_income_tax(self, tax: str) -> float:
        """
        Validate the State Income Tax from form 1099

        :param tax: State Income Tax from form 1099
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        pass

    def validate_other_states(self, other_states):
        """
        Validate the Income and Income Tax from other states.
        Uses validate_state_income() and validate_state_income_tax()
        :param other_states: List of other states
        :return: Validate list of other states
        :raises ValueError: Functions called will raise a ValueError with an
        appropriate message.
        """
        pass
