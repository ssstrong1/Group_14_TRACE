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





