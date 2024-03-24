import sqlite3

# connect to or creates sqlite db
user_connection = sqlite3.connect('tax_calculator.db')

# cursor obj to execute queries
user_cursor = user_connection.cursor()

# creating users table
user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL, 
        password TEXT NOT NULL
    )
''')

# creating the tax calc table
user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS jk (
        essn TEXT NOT NULL,
        ein TEXT NOT NULL,
        employer_name_etc TEXT NOT NULL,
        control_number TEXT NOT NULL,
        employee_first_i TEXT NOT NULL,
        employee_last TEXT NOT NULL,
        employee_suffix TEXT NOT NULL,
        employee_address_z TEXT NOT NULL,
        state TEXT NOT NULL,
        employers_state_id TEXT NOT NULL,
        state_wages_tips_etc TEXT NOT NULL,
        state_income_tax TEXT NOT NULL,
        local_wages_tips_etc TEXT NOT NULL,
        local_income_tax TEXT NOT NULL,
        locality_name TEXT NOT NULL,
        wages_tips_other_compensation TEXT NOT NULL,
        social_security_wages TEXT NOT NULL,
        medicare_wages_tips TEXT NOT NULL,
        social_security_tips TEXT NOT NULL,
        non_qualified_plans TEXT NOT NULL,
        other TEXT NOT NULL,
        federal_income_tax_withheld TEXT NOT NULL,
        social_security_tax_withheld TEXT NOT NULL,
        medicare_tax_withheld TEXT NOT NULL,
        allocated_tips TEXT NOT NULL,
        dependent_care_benefits TEXT NOT NULL,
        twelve_a TEXT NOT NULL,
        twelve_b TEXT NOT NULL,
        twelve_c TEXT NOT NULL,
        twelve_d TEXT NOT NULL,
        
        x TEXT NOT NULL,
        ten_forty_your_first_name_and_middle_initial TEXT NOT NULL, 
        ten_forty_your_last_name TEXT NOT NULL,
        ten_forty_if_joint_return_spouses_first_name_and_middle_initial TEXT NOT NULL,
        ten_forty_if_joint_last_name TEXT NOT NULL,
        ten_forty_home_address_number_and_street TEXT NOT NULL,
        ten_forty_apt_no TEXT NOT NULL,
        ten_forty_city_town_or_post_office TEXT NOT NULL, 
        ten_forty_state TEXT NOT NULL,
        ten_forty_zip_code TEXT NOT NULL,
        ten_forty_foreign_country_name TEXT NOT NULL, 
        ten_forty_foreign_province_state_county TEXT NOT NULL,    
        ten_forty_foreign_postal_code TEXT NOT NULL,
        ten_forty_dependents_first_name_1 TEXT NOT NULL,
        ten_forty_dependents_first_name_2 TEXT NOT NULL,
        ten_forty_dependents_first_name_3 TEXT NOT NULL,
        ten_forty_dependents_first_name_4 TEXT NOT NULL,
        ten_forty_total_amount_from_forms_w2_box_1 TEXT NOT NULL, 
        ten_forty_household_employee_wages_not_reported_on_forms_w2 TEXT NOT NULL,
        ten_forty_tip_income_not_reported_on_line_1a TEXT NOT NULL,
        ten_forty_medicaid_waiver_payments_not_reported_on_forms_w2 TEXT NOT NULL,
        ten_forty_taxable_dependent_care_benefits_from_form_2441_line_26 TEXT NOT NULL, 
        ten_forty_employer_provided_adoption_benefits_from_form_8839_line_29 TEXT NOT NULL,
        ten_forty_wages_from_form_8919_line_6 TEXT NOT NULL,
        ten_forty_other_earned_income TEXT NOT NULL,
        ten_forty_non_taxable_combat_pay_election TEXT NOT NULL,
        ten_forty_add_lines_1a_through_1h TEXT NOT NULL,
        ten_forty_tax_exempt_interest TEXT NOT NULL,
        ten_forty_qualified_dividends TEXT NOT NULL,
        ten_forty_ira_distributions TEXT NOT NULL,
        ten_forty_pensions_and_annuities TEXT NOT NULL, 
        ten_forty_social_security_benefits TEXT NOT NULL,
        ten_forty_taxable_interest TEXT NOT NULL,
        ten_forty_ordinary_dividends TEXT NOT NULL, 
        ten_forty_taxable_amount_4b TEXT NOT NULL,
        ten_forty_taxable_amount_5b TEXT NOT NULL,
        ten_forty_taxable_amount_6b TEXT NOT NULL,
        ten_forty_capital_gain_or_loss_attach_schedule_d_if_required TEXT NOT NULL, 
        ten_forty_additional_income_from_schedule_1_line_10 TEXT NOT NULL, 
        ten_forty_add_lines_1z_2b_3b_4b_5b_6b_7_8_this_is_your_total_income TEXT NOT NULL,
        ten_forty_adjustments_to_income_from_schedule_1_line_26 TEXT NOT NULL,
        ten_forty_subtract_line_10_from_line_9_this_is_your_adjusted_gross_income TEXT NOT NULL,
        ten_forty_standard_deduction_or_itemized_deductions_from_schedule_a TEXT NOT NULL,
        ten_forty_qualified_business_income_deduction_from_form_8995_or_form_8995_a TEXT NOT NULL, 
        ten_forty_add_lines_12_and_13 TEXT NOT NULL,
        ten_forty_subtract_line_14_from_line_11_if_zero_or_less_enter_0_this_is_your_taxable_income TEXT NOT NULL,
        ten_forty_form_no TEXT NOT NULL,
        ten_forty_tax_check_if_any_from_forms TEXT NOT NULL,
        ten_forty_amount_from_schedule_2_line_3 TEXT NOT NULL,
        ten_forty_add_lines_16_and_17 TEXT NOT NULL,
        ten_forty_child_tax_credit_or_credit_for_other_dependents_from_schedule_8812 TEXT NOT NULL, 
        ten_forty_amount_from_schedule_3_line_8 TEXT NOT NULL, 
        ten_forty_add_lines_19_and_20 TEXT NOT NULL, 
        ten_forty_subtract_line_21_from_line_18_if_zero_or_less_enter_0 TEXT NOT NULL,
        ten_forty_other_taxes_including_self_employment_tax_from_schedule_2_line_21 TEXT NOT NULL,
        ten_forty_add_lines_22_and_23_this_is_your_total_tax TEXT NOT NULL, 
        ten_forty_forms_w2 TEXT NOT NULL,
        ten_forty_forms_1099 TEXT NOT NULL, 
        ten_forty_other_forms TEXT NOT NULL,
        ten_forty_add_lines_25a_through_25c TEXT NOT NULL, 
        ten_forty_2023_estimated_tax_payments_and_amount_applied_from_2022_return TEXT NOT NULL,
        ten_forty_earned_income_credit TEXT NOT NULL,
        ten_forty_additional_child_tax_credit_from_schedule_8812 TEXT NOT NULL,
        ten_forty_american_opportunity_credit_from_form_8863_line_8 TEXT NOT NULL, 
        ten_forty_amount_from_schedule_3_line_15 TEXT NOT NULL, 
        ten_forty_add_lines_27_28_29_31_these_are_your_total_other_payments_refundable_credits TEXT NOT NULL,
        ten_forty_add_lines_25d_26_32_these_are_your_total_payments TEXT NOT NULL, 
        ten_forty_if_line_33_is_more_than_line_24_subtract_line_24_from_line_33_this_is_the_amount_you_overpaid TEXT NOT NULL,
        ten_forty_subtract_line_33_from_line_24_this_is_the_amount_you_owe TEXT NOT NULL,
        ten_forty_estimated_tax_penalty TEXT NOT NULL
        
    )
''')

user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS ten_nine (

        ten_ninety_nine_payers_name_etc TEXT NOT NULL,
        ten_ninety_nine_payers_tin TEXT NOT NULL,
        ten_ninety_nine_recipients_tin TEXT NOT NULL,
        ten_ninety_nine_recipients_name TEXT NOT NULL,
        ten_ninety_nine_street_address TEXT NOT NULL,
        ten_ninety_nine_city_town_etc TEXT NOT NULL,
        ten_ninety_nine_account_number TEXT NOT NULL,
        ten_ninety_nine_total_ordinary_dividends TEXT NOT NULL,
        ten_ninety_nine_qualified_dividends TEXT NOT NULL,
        ten_ninety_nine_total_capital_gain_dist TEXT NOT NULL,
        ten_ninety_nine_section_1202_gain TEXT NOT NULL, 
        ten_ninety_nine_section_897_ordinary_dividends TEXT NOT NULL,
        ten_ninety_nine_non_dividend_distributions TEXT NOT NULL,
        ten_ninety_nine_section_199A_dividends TEXT NOT NULL,
        ten_ninety_nine_foreign_tax_paid TEXT NOT NULL,
        ten_ninety_nine_cash_liquidation_distributions TEXT NOT NULL,
        ten_ninety_nine_exempt_interest_dividends TEXT NOT NULL,
        ten_ninety_nine_state TEXT NOT NULL,
        ten_ninety_nine_state_identification_no TEXT NOT NULL,
        ten_ninety_nine_un_recap_sec_1250_gain TEXT NOT NULL,
        ten_ninety_nine_collectibles_28_percent_gain TEXT NOT NULL, 
        ten_ninety_nine_section_897_capital_gain TEXT NOT NULL,
        ten_ninety_nine_federal_income_tax_withheld TEXT NOT NULL,
        ten_ninety_nine_investment_expenses TEXT NOT NULL, 
        ten_ninety_nine_foreign_country_or_us_possession TEXT NOT NULL,
        ten_ninety_nine_non_cash_liquidation_distributions TEXT NOT NULL,
        ten_ninety_nine_specified_private_activity_bond_interest_dividends TEXT NOT NULL,
        ten_ninety_nine_state_tax_withheld TEXT NOT NULL

    )
''')

# commit
user_connection.commit()

