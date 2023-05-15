from datetime import datetime
import pytest

from oneiro.loan import SimpleLoan

@pytest.fixture
def setup(monkeypatch):
    class MockSimpleLoan:
        def __init__(self, start_date, end_date, principal, currency, base_rate, margin):
            self.start_date = start_date
            self.end_date = end_date
            self.principal = principal
            self.currency = currency
            self.base_rate = base_rate
            self.margin = margin

        def get_interest_rate(self):
            return self.base_rate + self.margin

    monkeypatch.setattr('oneiro.loan', MockSimpleLoan)
    

loan = SimpleLoan(start_date='2022-01-01', end_date='2022-12-31', principal=20000,
                  currency='USD', base_rate=0.05, margin=0.02)


def test_loan_calculation_returns_daily_interest_no_margin():
    day_of_calculation = datetime.strptime('2022-05-01', '%Y-%m-%d')
    delta = day_of_calculation -datetime.strptime(loan.start_date, '%Y-%m-%d')
    
    expected_result = 0.025/365

    assert SimpleLoanCalculator.daily_base_interest_accrual(loan) == expected_result