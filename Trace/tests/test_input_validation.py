# test_input_validation.py
"""
Pytest unit testing for input_validation.py
"""
import pytest
from Trace.input_validation import (
    FormValidatorW2,
    FormValidator1099DIV,
    FormValidator1040
)


@pytest.fixture
def setup_validator_w2():
    """
    Fixture setup for W2 Form validator

    :return: initialized instance of the form validator
    """
    validator = FormValidatorW2()
    return validator


@pytest.fixture
def setup_validator_1099_div():
    """
    Fixture setup for 1099-DIV Form validator

    :return: initialized instance of the form validator
    """
    validator = FormValidator1099DIV()
    return validator


@pytest.fixture
def setup_validator_1040():
    """
    Fixture setup for 1040 Form validator

    :return: initialized instance of the form validator
    """
    validator = FormValidator1040()
    return validator


# W2
def test_validate_essn(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_essn("test")
        setup_validator_w2.validate_essn("-1")


def test_validate_ein(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_ein("test")
        setup_validator_w2.validate_ein("-1")


def test_validate_employer_name_etc(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_employer_name_etc("test#")


def test_validate_cn(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_cn("test")
        setup_validator_w2.validate_cn("-1")


def test_validate_employee_name_i(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_employee_name_i("test#")


def test_validate_employee_last(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_essn("test#")


def test_validate_address_zip(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_employee_address_zip("test#")


def test_validate_state_w2(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_state("test#")


def test_validate_wages_tips_other_comp(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_wages_tips_other_comp("test")
        setup_validator_w2.validate_wages_tips_other_comp("-1")


def test_validate_federal_income_tax_withheld(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_federal_income_tax_withheld("test")
        setup_validator_w2.validate_federal_income_tax_withheld("-1")


def test_validate_social_security_wages(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_social_security_wages("test")
        setup_validator_w2.validate_social_security_wages("-1")


def test_validate_social_security_tax(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_social_security_tax("test")
        setup_validator_w2.validate_social_security_tax("-1")


def test_validate_medicare_wages(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_medicare_wages("test")
        setup_validator_w2.validate_medicare_wages("-1")


def test_validate_medicare_tax(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_medicare_tax("test")
        setup_validator_w2.validate_medicare_tax("-1")


def test_validate_social_security_tips(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_social_security_tips("test")
        setup_validator_w2.validate_social_security_tips("-1")


def test_validate_allocated_tips(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_allocated_tips("test")
        setup_validator_w2.validate_allocated_tips("-1")


def test_validate_dependent_care_benefits(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_dependant_care_benefits("test")
        setup_validator_w2.validate_dependant_care_benefits("-1")


def test_validate_nonqualified_plans(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_nonqualified_plans("test")
        setup_validator_w2.validate_nonqualified_plans("-1")


def test_validate_12a(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_12a("test")
        setup_validator_w2.validate_12a("-1")


def test_validate_12b(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_12b("test")
        setup_validator_w2.validate_12b("-1")


def test_validate_12c(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_12c("test")
        setup_validator_w2.validate_12c("-1")


def test_validate_12d(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_12d("test")
        setup_validator_w2.validate_12d("-1")


def test_validate_state_wages_tips(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_state_wages_tips("test")
        setup_validator_w2.validate_state_wages_tips("-1")


def test_validate_state_income_tax(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_state_income_tax("test")
        setup_validator_w2.validate_state_income_tax("-1")


def test_validate_local_income(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_local_income("test")
        setup_validator_w2.validate_local_income("-1")


def test_validate_local_income_tax(setup_validator_w2):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_w2.validate_local_income_tax("test")
        setup_validator_w2.validate_local_income_tax("-1")


def test_validate_other_states_w2(setup_validator_w2):
    pass


# 1099-DIV
def test_validate_payer_name_etc(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_payer_name_etc("test#")


def test_validate_payer_tin(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_payer_tin("test")
        setup_validator_1099_div.validate_payer_tin("-1")


def test_validate_recipient_tin(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_recipient_tin("test")
        setup_validator_1099_div.validate_recipient_tin("-1")


def test_validate_recipient_name(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_recipient_name("test#")


def test_validate_recipient_address(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_recipient_address("test#")


def test_validate_recipient_city_etc(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_payer_tin("test#")


def test_validate_account_number(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_account_number("test")
        setup_validator_1099_div.validate_account_number("-1")


def test_validate_state_1099_div(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_state("test#")


def test_validate_state_id(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_state("test")
        setup_validator_1099_div.validate_state("-1")


def test_validate_ordinary_dividends(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_ordinary_dividends("test")
        setup_validator_1099_div.validate_ordinary_dividends("-1")


def test_validate_qualified_dividends(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_qualified_dividends("test")
        setup_validator_1099_div.validate_qualified_dividends("-1")


def test_validate_capital_gain_distr(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_capital_gain_distr("test")
        setup_validator_1099_div.validate_capital_gain_distr("-1")


def test_validate_unrecap_sec_1250_gain(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_unrecap_sec_1250_gain("test")
        setup_validator_1099_div.validate_unrecap_sec_1250_gain("-1")


def test_validate_section_1202_gain(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_section_1202_gain("test")
        setup_validator_1099_div.validate_section_1202_gain("-1")


def test_validate_collectibles_gain(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_collectibles_gain("test")
        setup_validator_1099_div.validate_collectibles_gain("-1")


def test_validate_section_897_ordinary_dividends(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_section_897_ordinary_dividends("test")
        setup_validator_1099_div.validate_section_897_ordinary_dividends("-1")


def test_validate_section_897_capital_gain(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_section_897_capital_gain("test")
        setup_validator_1099_div.validate_section_897_capital_gain("-1")


def test_validate_nondividend_distributions(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_nondividend_distributions("test")
        setup_validator_1099_div.validate_nondividend_distributions("-1")


def test_validate_income_tax_withheld(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_income_tax_withheld("test")
        setup_validator_1099_div.validate_income_tax_withheld("-1")


def test_validate_section_199a_dividends(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_section_199a_dividends("test")
        setup_validator_1099_div.validate_section_199a_dividends("-1")


def test_validate_investment_expenses(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_investment_expenses("test")
        setup_validator_1099_div.validate_investment_expenses("-1")


def test_validate_foreign_tax_paid(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_foreign_tax_paid("test")
        setup_validator_1099_div.validate_foreign_tax_paid("-1")


def test_validate_foreign_country_or_us_possession(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_foreign_country_or_us_possession("test")
        setup_validator_1099_div.validate_foreign_country_or_us_possession("-1")


def test_validate_cash_liquidation_distributions(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_cash_liquidation_distributions("test")
        setup_validator_1099_div.validate_cash_liquidation_distributions("-1")


def test_validate_noncash_liquidation_distributions(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_noncash_liquidation_distributions("test")
        setup_validator_1099_div.validate_noncash_liquidation_distributions("-1")


def test_validate_exempt_interest_dividends(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_exempt_interest_dividends("test")
        setup_validator_1099_div.validate_exempt_interest_dividends("-1")


def test_validate_private_activity_bond_interest_dividends(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_private_activity_bond_interest_dividends("test")
        setup_validator_1099_div.validate_private_activity_bond_interest_dividends("-1")


def test_validate_other_states_tax(setup_validator_1099_div):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1099_div.validate_other_states_tax("test")
        setup_validator_1099_div.validate_other_states_tax("-1")


def test_validate_other_states_1099_div(setup_validator_1099_div):
    pass


# 1040
def test_validate_first_name_i(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_first_name_i("test#")


def test_validate_last_name(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_last_name("test#")


def test_validate_spouse_first_i(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_spouse_first_i("test#")


def test_validate_spouse_last_name(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_spouse_last_name("test#")


def test_validate_home_address(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_home_address("test#")


def test_validate_apt_no(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_apt_no("test")
        setup_validator_1040.validate_apt_no("-1")


def test_validate_city_etc(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_city_etc("test#")


def test_validate_state_1040(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_state("test#")


def test_validate_zip_code(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_zip_code("test")
        setup_validator_1040.validate_zip_code("-1")


def test_validate_foreign_country_name(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_foreign_country_name("test#")


def test_validate_foreign_province(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_foreign_province("test#")


def test_validate_postal_code(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_foreign_postal_code("test")
        setup_validator_1040.validate_foreign_postal_code("-1")


def test_validate_dependents_first_last_1(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_dependets_first_last_1("test#")


def test_validate_dependents_first_last_2(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_dependets_first_last_2("test#")


def test_validate_dependents_first_last_3(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_dependets_first_last_3("test#")


def test_validate_dependents_first_last_4(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_dependets_first_last_4("test#")


def test_validate_filing_status(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    assert setup_validator_1040.validate_filing_status("Single"), "Entered, filing_status: Single"
    assert setup_validator_1040.validate_filing_status("Married Filing Jointly"), "Entered filing_status: Married Filing Jointly"
    assert setup_validator_1040.validate_filing_status("Married Filing Separately"), "Entered filing_status: Married Filing Separately"
    assert setup_validator_1040.validate_filing_status("Head of Household"), "Entered filing_status: Head of Household"
    assert setup_validator_1040.validate_filing_status("Qualifying Surviving Spouse"), "Entered filing_status: Qualifying Surviving Spouse"

    with pytest.raises(ValueError):
        setup_validator_1040.validate_filing_status("test")


def test_validate_user_age(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_user_age("test")
        setup_validator_1040.validate_user_age("-1")


def test_validate_spouse_age(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_spouse_age("test")
        setup_validator_1040.validate_spouse_age("-1")


def test_validate_income_w2(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_income_w2("test")
        setup_validator_1040.validate_income_w2("-1")


def test_validate_household_employee_income(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_household_employee_income("test")
        setup_validator_1040.validate_household_employee_income("-1")


def test_validate_tip_income(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_tip_income("test")
        setup_validator_1040.validate_tip_income("-1")


def test_validate_medicaid_waiver_payments(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_medicaid_waiver_payments("test")
        setup_validator_1040.validate_medicaid_waiver_payments("-1")


def test_validate_dependent_care_benefits_1040(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_dependent_care_benefits("test")
        setup_validator_1040.validate_dependent_care_benefits("-1")


def test_validate_employer_adoption_benefits(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_employer_adoption_benefits("test")
        setup_validator_1040.validate_employer_adoption_benefits("-1")


def test_validate_wages_form_8919(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_wages_form_8919("test")
        setup_validator_1040.validate_wages_form_8919("-1")


def test_validate_other_income(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_other_income("test")
        setup_validator_1040.validate_other_income("-1")


def test_validate_combat_pay(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_combat_pay("test")
        setup_validator_1040.validate_combat_pay("-1")


def test_validate_tax_exempt_interest(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_tax_exempt_interest("test")
        setup_validator_1040.validate_tax_exempt_interest("-1")


def test_validate_taxable_interest(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_taxable_interest("test")
        setup_validator_1040.validate_taxable_interest("-1")


def test_validate_qualified_dividends_1040(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_qualified_dividends("test")
        setup_validator_1040.validate_qualified_dividends("-1")


def test_validate_ordinary_dividends_1040(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_ordinary_dividends("test")
        setup_validator_1040.validate_ordinary_dividends("-1")


def test_validate_ira_distr(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_ira_distributions("test")
        setup_validator_1040.validate_ira_distributions("-1")


def test_validate_ira_taxable(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_ira_taxable("test")
        setup_validator_1040.validate_ira_taxable("-1")


def test_validate_pensions_annuities(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_pensions_annuities("test")
        setup_validator_1040.validate_pensions_annuities("-1")


def test_validate_pensions_annuities_taxable(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_pensions_annuities_taxable("test")
        setup_validator_1040.validate_pensions_annuities_taxable("-1")


def test_validate_ss_benefits(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_social_security_benefits("test")
        setup_validator_1040.validate_social_security_benefits("-1")


def test_validate_ss_benefits_taxable(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_ss_benefits_taxable("test")
        setup_validator_1040.validate_ss_benefits_taxable("-1")


def test_validate_capital_gain_loss(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_capital_gain_or_loss("test")
        setup_validator_1040.validate_capital_gain_or_loss("-1")


def test_validate_income_schedule_1(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_income_schedule_1("test")
        setup_validator_1040.validate_income_schedule_1("-1")


def test_validate_adjustments(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_adjustments("test")
        setup_validator_1040.validate_adjustments("-1")


def test_validate_qualified_income_business_deduction(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_qualified_business_income_deduction("test")
        setup_validator_1040.validate_qualified_business_income_deduction("-1")


def test_validate_form_no(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_form_no("test")
        setup_validator_1040.validate_form_no("-1")


def test_validate_tax(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_tax("test")
        setup_validator_1040.validate_tax("-1")


def test_validate_amount_schedule_2(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_amount_schedule_2("test")
        setup_validator_1040.validate_amount_schedule_2("-1")


def test_validate_child_tax_credit(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_child_tax_credit("test")
        setup_validator_1040.validate_child_tax_credit("-1")


def test_validate_amount_schedule_3_line_8(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_amount_schedule_3_line_8("test")
        setup_validator_1040.validate_amount_schedule_3_line_8("-1")


def test_validate_other_taxes(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_other_taxes("test")
        setup_validator_1040.validate_other_taxes("-1")


def test_validate_tax_withheld_w2(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_tax_withheld_w2("test")
        setup_validator_1040.validate_tax_withheld_w2("-1")


def test_validate_tax_withheld_1099(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_tax_withheld_1099("test")
        setup_validator_1040.validate_tax_withheld_1099("-1")


def test_validate_tax_withheld_other(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_tax_withheld_other("test")
        setup_validator_1040.validate_tax_withheld_other("-1")


def test_validate_estimate_tax_payments(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_estimate_tax_payments("test")
        setup_validator_1040.validate_estimate_tax_payments("-1")


def test_validate_earned_income_credit(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_earned_income_credit("test")
        setup_validator_1040.validate_earned_income_credit("-1")


def test_validate_additional_child_tax_credit(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_additional_child_tax_credit("test")
        setup_validator_1040.validate_additional_child_tax_credit("-1")


def test_validate_american_opportunity_credit(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_american_opportunity_credit("test")
        setup_validator_1040.validate_american_opportunity_credit("-1")


def test_validate_amount_schedule_3_line_15(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_amount_schedule_3_line_15("test")
        setup_validator_1040.validate_amount_schedule_3_line_15("-1")


def test_validate_penality(setup_validator_1040):
    """
    Test to ensure that validator raises an error for invalid input

    :return: N/A
    """
    with pytest.raises(ValueError):
        setup_validator_1040.validate_penality("test")
        setup_validator_1040.validate_penality("-1")




