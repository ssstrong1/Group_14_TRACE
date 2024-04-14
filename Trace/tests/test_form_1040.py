# test_form_1040.py

"""
Pytest unit testing for form_1040.py
"""

import pytest
import Trace.form_1040 as form_1040


@pytest.fixture
def setup_value():
    """
    Test value to be used as a default
    :return: test value
    """
    test_value = 1
    return test_value


@pytest.fixture
def setup_form_w2():
    """
    Fixture setup, initialize instance of form W-2
    :return: Form W-2 test data
    """
    w2_1 = {"WAGES_TIPS_OTHER_COMP": 98500.00, "FEDERAL_INCOME_TAX_WITHHELD": 15000.00,
               "SOCIAL_SECURITY_WAGES": 100000.00, "SOCIAL_SECURITY_TAX_WITHHELD": 5000.00,
               "MEDICARE_WAGES_AND_TIPS": 100000.00, "MEDICARE_TAX_WITHHELD": 1100.00,
               "DEPENDANT_CARE_BENEFITS": 0000,
               "STATES":
                   [{"STATE": "NC", "STATE_INCOME": 100000.00, "STATE_TAX_WITHHELD": 3000}]}
    w2_2 = {"WAGES_TIPS_OTHER_COMP": 98500.00, "FEDERAL_INCOME_TAX_WITHHELD": 15000.00,
               "SOCIAL_SECURITY_WAGES": 100000.00, "SOCIAL_SECURITY_TAX_WITHHELD": 5000.00,
               "MEDICARE_WAGES_AND_TIPS": 100000.00, "MEDICARE_TAX_WITHHELD": 1100.00,
               "DEPENDANT_CARE_BENEFITS": 0000,
               "STATES":
                   [{"STATE": "NC", "STATE_INCOME": 100000.00, "STATE_TAX_WITHHELD": 3000}]}

    test_w2 = [w2_1, w2_2]

    return test_w2


@pytest.fixture
def setup_form_1099_div():
    """
    Fixture setup, initialize instance of form 1099-DIV
    :return: Form 1099-DIV test data
    """
    test_1099_div = {"ORDINARY_DIVIDENDS": 20000.00,
                     "QUALIFIED_DIVIDENDS": 12000.00,
                     "CAPITAL_GAIN_DISTR": 11000.00, "UNRECAP_SEC_1250_GAIN": 10000.00,
                     "SECTION_1202_GAIN": 2000.00, "COLLECTIBLES_GAIN": 1000.00,
                     "SECTION_897_ORDINARY_DIVIDENDS": 2500.00, "SECTION_897_CAPITAL_GAIN": 1500.00,
                     "NONDIVIDEND_DISTRIBUTIONS": 23000.00, "INCOME_TAX_WITHHELD": 2000.00,
                     "SECTION_1999A_DIVIDENDS": 1590.75, "INVESTMENT_EXPENSES": 2456.00,
                     "FOREIGN_TAX_PAID": 9000.00, "FOREIGN_COUNTRY_OR_US_POSSESSION": 1200.00,
                     "CASH_LIQUIDATION_DISTRIBUTIONS": 2800.00, "NONCASH_LIQUIDATION_DISTRIBUTIONS": 1200.00,
                     "EXEMPT_INTEREST_DIVIDENDS": 7000.00, "PRIVATE_ACTIVITY_BOND_INTEREST_DIVIDENDS": 3000.00,
                     "FED_TAX_WITHHELD": 400.00}
    return test_1099_div


@pytest.fixture
def setup_form_1040(setup_form_w2, setup_form_1099_div, setup_value):
    """
    Fixture setup, initialize instance of form 1040
    :return: Form 1040 test data
    """
    test_1040 = form_1040.Form1040(forms_w2=setup_form_w2, form_1099_div=setup_form_1099_div)

    # Assign test income values
    test_1040.set_income_w2(setup_value)
    test_1040.set_household_employee_wages(setup_value)
    test_1040.set_tip_income(setup_value)
    test_1040.set_medicaid_waiver_payments(setup_value)
    test_1040.set_dependent_care_benefits(setup_value)
    test_1040.set_employer_adoption_benefits(setup_value)
    test_1040.set_wages_form_8919(setup_value)
    test_1040.set_other_income(setup_value)
    test_1040.set_taxable_interest(setup_value)
    test_1040.set_ordinary_dividends(setup_value)
    test_1040.set_ira_taxable(setup_value)
    test_1040.set_pensions_annuities_taxable(setup_value)
    test_1040.set_ss_benefits_taxable(setup_value)
    test_1040.set_capital_gain_or_loss(setup_value)
    test_1040.set_income_schedule_1(setup_value)
    test_1040.set_adjustments(setup_value)
    # Assign test tax and credits values
    test_1040.set_tax(setup_value)
    test_1040.set_amount_schedule_2(setup_value)
    test_1040.set_child_tax_credit(setup_value)
    test_1040.set_amount_schedule_3_line_8(setup_value)
    test_1040.set_other_taxes(setup_value)
    # Assign test payments values
    test_1040.set_tax_withheld_w2(setup_value)
    test_1040.set_tax_withheld_1099(setup_value)
    test_1040.set_tax_withheld_other(setup_value)
    test_1040.set_earned_income_credit(setup_value)
    test_1040.set_additional_child_tax_credit(setup_value)
    test_1040.set_american_opportunity_credit(setup_value)
    test_1040.set_amount_schedule_3_line_15(setup_value)
    test_1040.set_estimate_tax_payments(setup_value)

    return test_1040


def test_total_forms_w2(setup_form_w2, setup_form_1040):
    """
    Ensure that total_forms_w2 functions properly
    :param setup_form_w2: pytest fixture with test data for w2 forms
    :param setup_form_1040: pytest fixture with test data for 1040 forms
    :return: N/A
    """
    total_income = (setup_form_w2[0]["WAGES_TIPS_OTHER_COMP"] +
                    setup_form_w2[1]["WAGES_TIPS_OTHER_COMP"])
    total_tax = (setup_form_w2[0]["FEDERAL_INCOME_TAX_WITHHELD"] +
                 setup_form_w2[1]["FEDERAL_INCOME_TAX_WITHHELD"])

    setup_form_1040.total_forms_w2(0, 0)

    assert setup_form_1040.get_income_w2() == total_income, "Expected: " + str(total_income) + " Returned: " + str(setup_form_1040.get_income_w2())
    assert setup_form_1040.get_tax_withheld_w2() == total_tax, "Expected: " + str(total_tax) + " Returned: " + str(setup_form_1040.get_tax_withheld_w2())


def test_total_forms_1099(setup_form_1099_div, setup_form_1040):
    """
    Ensure that total_forms_1099 functions properly

    :param setup_form_1099_div: pytest fixture with test data for 1099 forms
    :param setup_form_1040: pytest fixture with test data for 1040 forms
    :return: N/A
    """
    #tax = setup_form_1099_div[0]["INCOME_TAX_WITHHELD"]

    #setup_form_1040.total_forms_1099(0)

    #assert setup_form_1040.get_tax_withheld_1099() == tax, "Expected: " + str(tax) + " Returned: " + str(setup_form_1040.get_tax_withheld_1099())
    pass


def test_total_lines_1a_to_1h(setup_form_1040, setup_value):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    total = setup_value * 8

    setup_form_1040.total_lines_1a_to_1h()

    assert setup_form_1040.get_total_1a_to_1h() == total, "Expected: " + str(total) + " Returned: " + str(setup_form_1040.get_total_1a_to_1h())


def test_calc_total_income(setup_form_1040, setup_value):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    total = setup_value * 15

    setup_form_1040.total_lines_1a_to_1h()
    setup_form_1040.calc_total_income()

    assert setup_form_1040.get_total_income() == total


def test_calc_agi(setup_form_1040, setup_value):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.total_lines_1a_to_1h()
    setup_form_1040.calc_total_income()

    total = setup_value * 15
    total = total - setup_value

    setup_form_1040.calc_adjusted_gross_income()

    assert setup_form_1040.get_adjusted_gross_income() == total


def test_calc_standard_deduction(setup_form_1040, setup_value):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.total_lines_1a_to_1h()
    setup_form_1040.calc_total_income()

    """
    If the user or spouse can be claimed as a dependent
    """
    setup_form_1040.set_is_dependent(True)
    setup_form_1040.set_user_age(60)
    setup_form_1040.set_user_is_blind(True)
    setup_form_1040.set_spouse_age(65)
    setup_form_1040.set_spouse_is_blind(False)

    # Total income < 850
    setup_form_1040.calc_standard_deduction()

    # Total income > 850
    setup_form_1040.set_income_schedule_1(1000)
    setup_form_1040.calc_total_income()
    setup_form_1040.calc_standard_deduction()

    """
    If the user and spouse cannot be claimed as a dependent
    """
    setup_form_1040.set_is_dependent(False)

    # Checks > 0, for seniors or the blind
    setup_form_1040.calc_standard_deduction()

    # Checks < 0, for anyone under 65 and NOT blind
    setup_form_1040.set_user_is_blind(False)
    setup_form_1040.set_spouse_age(55)
    setup_form_1040.calc_standard_deduction()


def test_calc_total_deductions(setup_form_1040, setup_value):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.total_lines_1a_to_1h()
    setup_form_1040.calc_total_income()
    setup_form_1040.calc_standard_deduction()
    setup_form_1040.set_qualified_business_income_deduction(setup_value)

    setup_form_1040.calc_total_deductions()


def test_calc_taxable_income(setup_form_1040, setup_value):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.total_lines_1a_to_1h()
    setup_form_1040.calc_total_income()
    setup_form_1040.calc_standard_deduction()
    setup_form_1040.set_qualified_business_income_deduction(setup_value)
    setup_form_1040.calc_total_deductions()
    setup_form_1040.calc_adjusted_gross_income()

    setup_form_1040.calc_taxable_income()


def test_calc_total_16_17(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_16_17()


def test_calc_total_19_20(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_19_20()


def test_calc_sub_21_18(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_16_17()
    setup_form_1040.calc_total_19_20()
    setup_form_1040.calc_sub_21_18()


def test_calc_total_tax(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_16_17()
    setup_form_1040.calc_total_19_20()
    setup_form_1040.calc_sub_21_18()

    setup_form_1040.calc_total_tax()


def test_calc_total_withheld(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_withheld()


def test_calc_total_other_payments(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_other_payments()


def test_calc_total_payments(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_withheld()
    setup_form_1040.calc_total_other_payments()
    setup_form_1040.calc_total_payments()


def test_calc_refund(setup_form_1040):
    """
    Ensure that total_lines_1a_to_1h functions correctly

    :param setup_form_1040: pytest fixture with test data for 1040 form
    :return: N/A
    """
    setup_form_1040.calc_total_16_17()
    setup_form_1040.calc_total_19_20()
    setup_form_1040.calc_sub_21_18()
    setup_form_1040.calc_total_tax()

    setup_form_1040.calc_total_withheld()
    setup_form_1040.calc_total_other_payments()
    setup_form_1040.calc_total_payments()

    # User overpaid
    setup_form_1040.calc_refund()
    assert setup_form_1040.get_overpaid() == 7

    # User owes additional dues
    setup_form_1040.set_tax(100)
    setup_form_1040.calc_total_16_17()
    setup_form_1040.calc_total_19_20()
    setup_form_1040.calc_sub_21_18()
    setup_form_1040.calc_total_tax()
    setup_form_1040.calc_refund()
    assert setup_form_1040.get_amount_owed() == 92







