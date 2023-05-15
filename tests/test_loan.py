import pytest


@pytest.fixture
def loan():
    return Loan(start_date="2012-02-15", end_date="2022-02-15", principal=10000, currency="USD", base_rate=4.5, margin=2)

def test_loan_has_correct_attributes(loan):
    assert loan.start_date == "2012-02-15"
    assert loan.end_date == "2022-02-15"
    assert loan.principal == 1000
    assert loan.currency == "USD"
    assert loan.base_rate == 4.5
    assert loan.margin == 2


