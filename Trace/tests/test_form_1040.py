# test_form_1040.py

"""
Pytest unit testing for form_1040.py
"""

import pytest


@pytest.fixture
def setup_form_w2():
    """
    Fixture setup, initialize instance of form W-2
    :return: Form W-2 test data
    """
    pass

@pytest.fixture
def setup_form_1099_div():
    """
    Fixture setup, initialize instance of form 1099-DIV
    :return: Form 1099-DIV test data
    """
    pass

@pytest.fixture
def setup_form_1040(setup_form_w2, setup_form_1099_div):
    """
    Fixture setup, initialize instance of form 1040
    :return: Form 1040 test data
    """
    pass

