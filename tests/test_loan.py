import pytest

from oneiro.loan import SimpleLoan


@pytest.fixture
def simple_loan():
    return SimpleLoan(start_date="2012-02-15", end_date="2022-02-15", principal=10000.10, currency="USD", base_rate=4.5, margin=2)

def test_loan_has_correct_attributes(simple_loan):
    assert simple_loan.start_date == "2012-02-15"
    assert simple_loan.end_date == "2022-02-15"
    assert simple_loan.principal == 10000.1
    assert simple_loan.currency == "USD"
    assert simple_loan.base_rate == 4.5
    assert simple_loan.margin == 2

