# 1099
ten_ninety_nine_payer_info = ""
ten_ninety_nine_payer_tin = ""
ten_ninety_nine_recipient_tin, ten_ninety_nine_recipient_name = "", ""
ten_ninety_nine_recipient_address = ""
ten_ninety_nine_recipient_city_etc = ""
ten_ninety_nine_account_number = ""
ten_ninety_nine_ordinary_dividends = ""
ten_ninety_nine_qualified_dividends = ""
ten_ninety_nine_capital_gain = ""
ten_ninety_nine_1250_gain, ten_ninety_nine_1202_gain = "", ""
ten_ninety_nine_collectibles_gain = ""
ten_ninety_nine_897_dividends, ten_ninety_nine_897_gain = "", ""
ten_ninety_nine_nondividend = ""
ten_ninety_nine_federal_tax_withheld, ten_ninety_nine_199a = 00.00, ""
ten_ninety_nine_investment_expenses = ""
ten_ninety_nine_foreign_tax, ten_ninety_nine_foreign_tax_country = "", ""
ten_ninety_nine_cash_liquidation = ""
ten_ninety_nine_noncash_liquidation = ""
ten_ninety_nine_exempt_dividends = ""
ten_ninety_nine_specified_bond_dividends = ""
ten_ninety_nine_state, ten_ninety_nine_state_id_number = "", ""
ten_ninety_nine_state_tax_withheld = ""

# W-2
essn_entry, ein_entry = "", ""
employer_name_etc, cn_entry, employee_name_i, employee_last_name = "", "", "", ""
employee_suffix, employee_address_etc = "", ""
state_field, employers_state_id, state_wage_tips, state_income_tax = "", "", "", ""
local_wage_tips, local_income_tax, locality_name, wages_tips_c = "", "", "", ""
social_wages, medicare_wages, social_security_tips = "", "", ""
non_qualified_plans, other_field, fed_income_tax_withheld = "", "", 00.00
social_security_tax_withheld, medicare_tax_withheld, allocated_tips = "", "", ""
dependent_care_benefits, twelve_a, twelve_b, twelve_c, twelve_d = "", "", "", "", ""

# 1040
ten_forty_first_name, ten_forty_last_name = "", ""
ten_forty_spouse_first, ten_forty_spouse_last = "", ""
ten_forty_home_address, ten_forty_apt_no, ten_forty_city = "", "", ""
ten_forty_state, ten_forty_zip, ten_forty_foreign_country = "", "", ""
ten_forty_foreign_province, ten_forty_foreign_post_code = "", ""

ten_forty_dependent_first_1, ten_forty_dependent_first_2 = "", ""
ten_forty_dependent_first_3 = ""
ten_forty_dependent_first_4 = ""

ten_forty_total_w2s, ten_forty_household_wages = 00.00, 00.00
ten_forty_tip_income = ""
ten_forty_medicaid_waiver, ten_forty_dependent_benefits = "", ""
ten_forty_adoption_benefits, ten_forty_8919_wages = "", ""
ten_forty_other_income = ""
ten_forty_combat_pay, ten_forty_1_ah_sum = "", ""
ten_forty_tax_exempt_interest = ""

ten_forty_taxable_interest, ten_forty_qualified_dividends = "", ""
ten_forty_ordinary_dividends, ten_forty_ira_distributions = "", ""
ten_forty_taxable_ira = ""
ten_forty_pensions_annuities, ten_forty_taxable_pensions = "", ""
ten_forty_social_security, ten_forty_social_taxable = "", ""
ten_forty_capital_gain = ""
ten_forty_schedule_1, ten_forty_total_income = "", ""
ten_forty_income_adjustments, ten_forty_adjusted_income = "", ""
ten_forty_deductions, ten_forty_business_deductions = "", ""
ten_forty_total_deductions = ""
ten_forty_taxable_income = ""
ten_forty_other_form_no = ""
ten_forty_other_form_total, ten_forty_schedule_2 = "", ""
ten_forty_add_16_17 = ""
ten_forty_child_credit, ten_forty_schedule_3, ten_forty_add_19_20 = "", "", ""
ten_forty_sub_21_18, ten_forty_other_taxes, ten_forty_total_tax = "", "", ""
ten_forty_withheld_w2, ten_forty_withheld_1099 = "", ""
ten_forty_withheld_other = ""
ten_forty_withheld_total, ten_forty_previous_year, ten_forty_eic = "", "", ""
ten_forty_8812_child_credit, ten_forty_8863_opportunity_credit = "", ""
ten_forty_schedule_3_line_15, ten_forty_other_payments = "", ""
ten_forty_total_payments = ""
ten_forty_overpaid, ten_forty_owed, ten_forty_penalty = "", "", ""

# 1040 checkboxes
ten_forty_presidential_you, ten_forty_presidential_spouse = "", ""
ten_forty_filing_single, ten_forty_filing_jointly = "", ""
ten_forty_filing_separately = ""
ten_forty_filing_hoh, ten_forty_filing_qss = "", ""
ten_forty_digital_assets_yes = ""
ten_forty_digital_assets_no, ten_forty_are_dependent = "", ""
ten_forty_spouse_dependent = ""
ten_forty_spouse_separate, ten_forty_self_1959 = "", ""
ten_forty_self_blind = ""
ten_forty_spouse_1959, ten_forty_spouse_blind = "", ""
ten_forty_many_dependents = ""
ten_forty_dependent_1_child_credit, ten_forty_dependent_1_other_credit = "", ""
ten_forty_dependent_2_child_credit, ten_forty_dependent_2_other_credit = "", ""
ten_forty_dependent_3_child_credit, ten_forty_dependent_3_other_credit = "", ""
ten_forty_dependent_4_child_credit, ten_forty_dependent_4_other_credit = "", ""
ten_forty_schedule_d = ""
ten_forty_lump_sum_method = ""
ten_forty_8814 = ""
ten_forty_4972 = ""
ten_forty_other_form_check = ""
ten_forty_8888 = ""
ten_forty_route_checking = ""
ten_forty_route_savings = ""
ten_forty_third_party_yes = ""
ten_forty_third_party_no = ""
ten_forty_self_employed = ""

# Totals
total_1a_to_1h = 00.00  # 1z, Total of lines 1a to 1h
total_income = 00.00  # 9, Total of lines 1z, 2b-6b, 7, and 8
adjusted_gross_income = 00.00  # 11, subtract line 10 from line 9
total_deductions = 00.00  # 14, add lines 12 and 13
taxable_income = 00.00  # 15, subtract line 14 from 11, if zero or less == 00.00
total_16_17 = 00.00  # 18, add lines 16 and 17
total_19_20 = 00.00  # 21, add lines 19 and 20
subtract_21_from_18 = 00.00  # 22, subtract line 21 from line 18, if zero or less == 00.00
total_tax = 00.00  # 24, add lines 22 and 23
total_withheld = 00.00  # 25d, total lines 25a to 25c
total_other_payments = 00.00  # 31, add lines 27 to 31
total_payments = 00.00  # 32, add lines 25d, 26, and 32
overpaid = 00.00  # 34, subtract line 24 from 33
amount_owed = 00.00  # 37, subtract line 33 from 24

example_c = 00.00

# Other Carriers/Lists/Totals
w2_group_of_fed_income_tax_withheld = []

ten_99_group_of_fed_income_tax_withheld = []

overall_total_w2_group_of_fed_income_tax_withheld = 00.00

overall_total_ten_99_group_of_fed_income_tax_withheld = 00.00

#def send_info(self):
#    info_attributes = [
#        "ten_ninety_nine_payer_info",
#        "ten_ninety_nine_payer_tin",
#        "ten_ninety_nine_recipient_tin",
#        "ten_ninety_nine_recipient_name",
#        "ten_ninety_nine_recipient_address",
#        "ten_ninety_nine_recipient_city_etc",
#        "ten_ninety_nine_account_number",
#        "ten_ninety_nine_ordinary_dividends",
#        "ten_ninety_nine_qualified_dividends",
#        "ten_ninety_nine_capital_gain",
#        "ten_ninety_nine_1250_gain",
#        "ten_ninety_nine_1202_gain",
#        "ten_ninety_nine_collectibles_gain",
#        "ten_ninety_nine_897_dividends",
#        "ten_ninety_nine_897_gain",
#        "ten_ninety_nine_nondividend"
#    ]#
#
#    for attr in info_attributes:
#        setattr(self, attr, getattr(all_user_info, attr))"""