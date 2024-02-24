# test_calculate_return.py
"""
Pytest unit testing for calculate_return.py
"""
import pytest
import test_calculate_return

@pytest.fixture
def setup_data_W2():
    """
    Fixture setup, initialize test data.
    :return: List of dictionary objects representing input from W-2 forms.
    """
    form_w2 = list()
    return form_w2

@pytest.fixture
def setup_data_1099():
    """
    Fixture setup, initialize test data.
    :return: List of dictionary objects representing input from 1099 forms.
    """
    form_1099 = list()
    return form_1099

def test_calculate_state_return(setup_data_W2, setup_data_1099):
    """
    Test to ensure accurate calculations from calculate_return.calculate_state_return
    :return:
    """
    pass
