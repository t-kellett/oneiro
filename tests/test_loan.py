from datetime import datetime
import pytest

from oneiro.simple_loan import SimpleLoan


@pytest.fixture
def simple_loan():
    return SimpleLoan(start_date_str="2012-02-15", end_date="2022-02-15", principal=10000.10, currency="USD", base_rate=0.045, margin=0.02)

def test_loan_has_correct_attributes(simple_loan):
    assert simple_loan.start_date_str == "2012-02-15"
    assert simple_loan.end_date == "2022-02-15"
    assert simple_loan.principal == 10000.1
    assert simple_loan.currency == "USD"
    assert simple_loan.base_rate == 0.045
    assert simple_loan.margin == 0.02


def test_loan_gets_total_interest_rate(simple_loan):
    assert simple_loan.get_total_interest() == 0.065


def test_loan_gets_correct_start_date(simple_loan):
    expected_date = datetime.strptime(simple_loan.start_date_str, '%Y-%m-%d')
    assert simple_loan.get_start_date() == expected_date