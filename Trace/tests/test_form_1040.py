# test_form_1040.py

"""
Pytest unit testing for form_1040.py
"""

import pytest
import Trace.form_1040 as form_1040


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
                     "STATES":
                         [{"STATE": "NC", "STATE_TAX_WITHHELD": 400.00}]}
    return test_1099_div


@pytest.fixture
def setup_form_1040():
    """
    Fixture setup, initialize instance of form 1040
    :return: Form 1040 test data
    """
    test_1040 = form_1040.Form1040()
    return test_1040


def test_total_forms_w2(setup_form_w2):
    """
    Assert that total_forms_w2 functions properly
    :param setup_form_w2:
    :return:
    """
    total_income = (setup_form_w2[0]["WAGES_TIPS_OTHER_COMP"] +
                    setup_form_w2[1]["WAGES_TIPS_OTHER_COMP"])
    total_tax = (setup_form_w2[0]["FEDERAL_INCOME_TAX_WITHHELD"] +
                 setup_form_w2[1]["FEDERAL_INCOME_TAX_WITHHELD"])
    pass
