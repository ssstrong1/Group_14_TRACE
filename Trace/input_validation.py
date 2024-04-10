# input_validation.py
from tkinter import messagebox
"""
Contains functions for validating user input.
Will require a separate validator function for each user input entry.
"""


class FormValidatorW2:
    """
    Class dedicated to validating W-2 Forms.

    Raises ValueErrors with specific messages if validation fails.
    """

    def validate_essn(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box a, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box a, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
        if value <= 0:
            messagebox.showerror("Error", "Invalid input for box a, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box a, must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_ein(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box b, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box b, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box b, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box b, must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_employer_name_etc(self, dollars: str) -> str:
        """
        Validate the input string for employer name, etc.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters, integers, a comma, and a space
            if not dollars.replace(',', '').replace(' ', '').isalnum():
                messagebox.showerror("Error", "Invalid input for box c, must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: Employer's Name, Address, Zip Code")

                raise ValueError("Invalid input for box c, must contain only the following: letters, numbers, and commas with spaces. No special characters.")

        except ValueError:
            raise ValueError("Invalid input for box c, must contain only the following: letters, numbers, and commas with spaces. No special characters.")

        return dollars


    def validate_cn(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box d, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box d, must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box d, must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box d, must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_employee_name_i(self, dollars: str) -> str:
        """
        Validate the input string for employee name.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box e, must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Employee's Name Intitial")

                raise ValueError("Invalid input for box e, must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Employee's Name Intitial")

        except ValueError:
            raise ValueError("Invalid input for box e, must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Employee's Name Intitial")

        return dollars

    def validate_employee_last(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box e (last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Employee's Last Name")
                raise ValueError("Invalid input for box e (last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Employee's Last Name")

        except ValueError:
            raise ValueError("Invalid input for box e (last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Employee's Last Name")

        return dollars

    def validate_employee_address_zip(self, dollars: str) -> str:
        """
        Validate the input string for employer name, etc.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters, integers, spaces
            if not dollars.replace(' ', '').isalnum():
                messagebox.showerror("Error", "Invalid input for box f, must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Employee's Address Zip Code")

                raise ValueError("Invalid input for box f, must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Employee's Address Zip Code")

        except ValueError:
            raise ValueError("Invalid input for box f, must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Employee's Address Zip Code")

        return dollars

    def validate_state(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box 15 (state), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")
                raise ValueError("Invalid input for box 15 (state), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")

        except ValueError:
            raise ValueError("Invalid input for box 15 (state), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")

        return dollars



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
            messagebox.showerror("Error", "Invalid input for box 1, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 3, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 3, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
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
            messagebox.showerror("Error", "Invalid input for box 4, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 4, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
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
            messagebox.showerror("Error", "Invalid input for box 5, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 5, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
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
            messagebox.showerror("Error", "Invalid input for box 6, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 6, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_social_security_tips(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 7, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 7, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_allocated_tips(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 8, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 8, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
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
            messagebox.showerror("Error", "Invalid input for box 10, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 10, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_nonqualified_plans(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 11, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 11, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_12a(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 12a, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 12a, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_12b(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 12b, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 12b, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_12c(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 12c, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 12c, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        return value

    def validate_12d(self, dollars: str) -> float:
        """
        Validate the Medicare Tax Withheld from form W-2

        :param dollars: Medicare Tax Withheld from form W-2
        :return: Validated tax value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 12d, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 12d, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")
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
            messagebox.showerror("Error", "Invalid input for box 16, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 16, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 17, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 17, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 18, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 18, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 19, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 19, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        return value

    def validate_other_states(self, other_states):
        """
        Validate the Income and Income Tax from other states.
        Uses validate_state_wages_tips() and validate_state_income_tax()
        :param other_states: List of other states
        :return: Validated list of other states
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

    def validate_payer_name_etc(self, dollars: str) -> str:
        """
        Validate the input string for employer name, etc.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters, integers, a comma, and a space
            if not dollars.replace(',', '').replace(' ', '').isalnum():
                messagebox.showerror("Error", "Invalid input for box (Payer's name, street address, etc.), must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: PAYER’S name, street address, city or town, state or province, country, ZIP or foreign postal code, and telephone no.")

                raise ValueError("Invalid input for box (Payer's name, street address, etc.), must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: PAYER’S name, street address, city or town, state or province, country, ZIP or foreign postal code, and telephone no.")

        except ValueError:
            raise ValueError("Invalid input for box f, must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: PAYER’S name, street address, city or town, state or province, country, ZIP or foreign postal code, and telephone no.")

        return dollars

    def validate_payer_tin(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (Payer's TIN), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Payer's TIN), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (Payer's TIN), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Payer's TIN), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_recipient_tin(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (Recipient's TIN), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Recipient's TIN), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (Recipient's TIN), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Recipient's TIN), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_recipient_name(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Recipient's name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Recipient's name")
                raise ValueError("Invalid input for box (Recipient's name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Recipient's name")

        except ValueError:
            raise ValueError("Invalid input for box (Recipient's name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Recipient's name")

        return dollars

    def validate_recipient_address(self, dollars: str) -> str:
        """
        Validate the input string for employer name, etc.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters, integers, spaces
            if not dollars.replace(' ', '').isalnum():
                messagebox.showerror("Error", "Invalid input for box (Street Address (including apt. no.)), must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Street Address (including apt. no.)")

                raise ValueError("Invalid input for box (Street Address (including apt. no.)), must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Street Address (including apt. no.)")

        except ValueError:
            raise ValueError("Invalid input for box (Street Address (including apt. no.)), must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Street Address (including apt. no.)")

        return dollars

    def validate_recipient_city_etc(self, dollars: str) -> str:
        """
        Validate the input string for employer name, etc.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters, integers, a comma, and a space
            if not dollars.replace(',', '').replace(' ', '').isalnum():
                messagebox.showerror("Error", "Invalid input for box (City or town, state or province, etc.), must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: City or town, state or province, country, and ZIP or foreign postal code")

                raise ValueError("Invalid input for box (City or town, state or province, etc.), must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: City or town, state or province, country, and ZIP or foreign postal code")

        except ValueError:
            raise ValueError("Invalid input for box (City or town, state or province, etc.), must contain only the following: letters, numbers, and commas with spaces. No special characters. Use the following format for the best desired output: City or town, state or province, country, and ZIP or foreign postal code")

        return dollars

    def validate_account_number(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (Account number (see instructions)), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Account number (see instructions)), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (Account number (see instructions)), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Account number (see instructions)), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_state(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box 14, must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")
                raise ValueError("Invalid input for box 14, must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")

        except ValueError:
            raise ValueError("Invalid input for box 14, must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")

        return dollars

    def validate_state_id(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (State identification no.), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (State identification no.), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (State identification no.), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (State identification no.), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

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
            messagebox.showerror("Error", "Invalid input for box 1a, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1a, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1b, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1b, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2a, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2a, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2b, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2b, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2c, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2c, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2d, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2d, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2e, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2e, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2f, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2f, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 3, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 3, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 4, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 4, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 5, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 5, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 6, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 6, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 7, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 7, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 8, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 8, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 9, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 9, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 10, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 10, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 12, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 12, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 13, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 13, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 16, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 16, must enter a positive number. If N/A put 0.")
            raise ValueError("Invalid input, must enter a positive number. If N/A put 0.")

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

    def validate_first_name_i(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Your first name and middle intitial), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Your first name and middle intitial")
                raise ValueError("Invalid input for box (Your first name and middle intitial), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Your first name and middle intitial")

        except ValueError:
            raise ValueError("Invalid input for box (Your first name and middle intitial), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Your first name and middle intitial")

        return dollars

    def validate_last_name(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Your Last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Your Last name")
                raise ValueError("Invalid input for box (Your Last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Your Last name")

        except ValueError:
            raise ValueError("Invalid input for box (Your Last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Your Last name")

        return dollars

    def validate_spouse_first_i(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (If joint return, spouse's first name and initial), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: If joint return, spouse's first name and initial")
                raise ValueError("Invalid input for box (If joint return, spouse's first name and initial), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: If joint return, spouse's first name and initial")

        except ValueError:
            raise ValueError("Invalid input for box (If joint return, spouse's first name and initial), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: If joint return, spouse's first name and initial")

        return dollars

    def validate_spouse_last_name(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Spouse's Last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Spouse's Last name")
                raise ValueError("Invalid input for box (Spouse's Last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Spouse's Last name")

        except ValueError:
            raise ValueError("Invalid input for box (Spouse's Last name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Spouse's Last name")

        return dollars

    def validate_home_address(self, dollars: str) -> str:
        """
        Validate the input string for employer name, etc.

        :param input_string: Input string to validate
        :return: Validated input string
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters, integers, spaces
            if not dollars.replace(' ', '').isalnum():
                messagebox.showerror("Error", "Invalid input for box (Home address (number and street). If you have a P.O. box, see instructions.), must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Home address (number and street). If you have a P.O. box, see instructions.")

                raise ValueError("Invalid input for box (Home address (number and street). If you have a P.O. box, see instructions.), must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Home address (number and street). If you have a P.O. box, see instructions.")

        except ValueError:
            raise ValueError("Invalid input for box (Home address (number and street). If you have a P.O. box, see instructions.), must contain only the following: letters, numbers, spaces. No special characters. Use the following format for the best desired output: Home address (number and street). If you have a P.O. box, see instructions.")

        return dollars

    def validate_apt_no(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (Apt no.), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Apt no.), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (Apt no.), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Apt no.), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_city_etc(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (City, town, or post office. If you have a foreign address, also complete spaces below.), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: City, town, or post office. If you have a foreign address, also complete spaces below.")
                raise ValueError("Invalid input for box (City, town, or post office. If you have a foreign address, also complete spaces below.), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: City, town, or post office. If you have a foreign address, also complete spaces below.")

        except ValueError:
            raise ValueError("Invalid input for box (City, town, or post office. If you have a foreign address, also complete spaces below.), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: City, town, or post office. If you have a foreign address, also complete spaces below.")

        return dollars

    def validate_state(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (State), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")
                raise ValueError("Invalid input for box (State), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")

        except ValueError:
            raise ValueError("Invalid input for box (State), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: State")

        return dollars

    def validate_zip_code(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (ZIP code), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (ZIP code), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (ZIP code), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (ZIP code), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_foreign_country_name(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Foreign country name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Foreign country name")
                raise ValueError("Invalid input for box (Foreign country name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Foreign country name")

        except ValueError:
            raise ValueError("Invalid input for box (Foreign country name), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Foreign country name")

        return dollars

    def validate_foreign_province(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Foreign province/state/county), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Foreign province/state/county")
                raise ValueError("Invalid input for box (Foreign province/state/county), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Foreign province/state/county")

        except ValueError:
            raise ValueError("Invalid input for box (Foreign province/state/county), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Foreign province/state/county")

        return dollars

    def validate_foreign_postal_code(self, dollars: str) -> int:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (Foreign postal code), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Foreign postal code), must enter a valid series of positive numbers. No special characters.")
        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (Foreign postal code), must enter a valid series of positive numbers. No special characters. If N/A put 0.")
            raise ValueError("Invalid input for box (Foreign postal code), must enter a valid series of positive numbers. No special characters. If N/A put 0.")

        return value

    def validate_dependets_first_last_1(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Dependents First 1), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 1")
                raise ValueError("Invalid input for box (Dependents First 1), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 1")

        except ValueError:
            raise ValueError("Invalid input for box (Dependents First 1), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 1")

        return dollars

    def validate_dependets_first_last_2(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Dependents First 2), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 2")
                raise ValueError("Invalid input for box (Dependents First 2), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 2")

        except ValueError:
            raise ValueError("Invalid input for box (Dependents First 2), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 2")

        return dollars

    def validate_dependets_first_last_3(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Dependents First 3), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 3")
                raise ValueError("Invalid input for box (Dependents First 3), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 3")

        except ValueError:
            raise ValueError("Invalid input for box (Dependents First 3), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 3")

        return dollars

    def validate_dependets_first_last_4(self, dollars: str) -> str:
        """
        Validate the Wages, Tips, and Other Compensation from form W-2

        :param dollars: Wages, Tips, and Other Compensation from form W-2
        :return: Validated wages value as a float
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            # Check if the input contains only letters and spaces
            if not dollars.replace(' ', '').isalpha():
                messagebox.showerror("Error", "Invalid input for box (Dependents First 4), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 4")
                raise ValueError("Invalid input for box (Dependents First 4), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 4")

        except ValueError:
            raise ValueError("Invalid input for box (Dependents First 4), must contain only the following: letters, spaces. No special characters. Use the following format for the best desired output: Dependents First 4")

        return dollars

    def validate_filing_status(self, status: str):
        """
        Validate filing_status from form 1040
        :param status: filing_status string
        :return: Validated status value as string
        :raises ValueError: If validation fails, with an appropriate error message
        """
        print(status)
        status_list = ["Single", "Married Filing Jointly", "Married Filing Separately",
                       "Head of Household", "Qualifying Surviving Spouse"]
        if status in status_list:
            return status
        else:
            messagebox.showerror("Error", "Invalid input, must select one valid filing status.")
            raise ValueError("Invalid input, must select one valid filing status.")

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
            raise ValueError("Invalid input, please enter a positive integer. If N/A put 0.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive integer. If N/A put 0.")

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
            raise ValueError("Invalid input, please enter a positive integer. If N/A put 0.")

        if value < 0:
            raise ValueError("Invalid input, please enter a positive integer. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1c, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1c, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1d, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1d, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1e, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1e, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1f, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1f, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1g, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1g, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1h, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1h, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 1i, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 1i, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 2b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 2b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 3a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 3a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 3b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 3b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 4a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 4a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 4b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 4b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 5a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 5a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 5b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 5b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 6a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 6a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 6b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 6b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 7, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 7, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 8, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 8, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 10, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 10, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 13, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 13, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        return value

    def validate_form_no(self, dollars: str) -> int:
        """
        Validate qualified_business_income_deduction from form 1040
        :param dollars: qualified business income deduction from form 1040 line 13
        :return: validated value as float
        """
        try:
            value = int(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box (Form No.), must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box (Form No.), must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 16, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 16, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 17, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 17, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 19, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 19, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 20, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 20, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 23, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 23, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 25a, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 25aa, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 25b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 25b, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 25c, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 25c, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 26, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 26, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 27, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 27, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 28, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 28, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 29, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 29, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

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
            messagebox.showerror("Error", "Invalid input for box 31, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 31, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        return value

    def validate_penality(self, dollars: str) -> float:
        """
        Validate amount_schedule_3_line_15 from form 1040
        :param dollars: amount from schedule 3 line 15 from form 1040 line 30
        :return: validated value as float
        """
        try:
            value = float(dollars)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for box 38, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        if value < 0:
            messagebox.showerror("Error", "Invalid input for box 38, must enter a positive number. If N/A put 0.")

            raise ValueError("Invalid input, please enter a positive number. If N/A put 0.")

        return value

