from datetime import datetime
import decimal
import pytest

from oneiro.simple_loan import SimpleLoan
from oneiro.simple_loan_calculator import SimpleLoanCalculator

@pytest.fixture
def setup(monkeypatch):
    class MockSimpleLoan:
        def __init__(self, start_date_str, end_date, principal, currency, base_rate, margin):
            self.start_date_str = start_date_str
            self.end_date = end_date
            self.principal = principal
            self.currency = currency
            self.base_rate = base_rate
            self.margin = margin

        def get_start_date(self):
            return datetime.strptime(self.start_date_str, '%Y-%m-%d')
        
        def get_total_interest(self) -> decimal:
            return self.base_rate + self.margin

    monkeypatch.setattr('oneiro.loan', MockSimpleLoan)
    
START_DATE = '2022-01-01'
END_DATE = '2022-12-31'

loan = SimpleLoan(start_date_str=START_DATE, end_date_str=END_DATE, principal=20000,
                  currency='USD', base_rate=0.05, margin=0.02)


def test_loan_calculator_gets_correct_loan_days():
    start = datetime.strptime(START_DATE, '%Y-%m-%d')
    end = datetime.strptime(END_DATE, '%Y-%m-%d')

    delta_days = (end - start).days

    assert SimpleLoanCalculator.get_loan_days(loan) == delta_days


def test_loan_calculator_gets_daily_interest_amount():
    day_of_calculation = datetime.strptime('2022-05-01', '%Y-%m-%d')
    delta = loan.get_end_date() - loan.get_start_date()

    expected_result = loan.base_rate/delta.days

    assert SimpleLoanCalculator.get_daily_base_interest(loan) == expected_result


def test_loan_calculation_returns_daily_interest_no_margin():
    day_of_calculation = datetime.strptime('2022-05-01', '%Y-%m-%d')
    delta = day_of_calculation - loan.get_start_date()
    
    expected_result = SimpleLoanCalculator.get_daily_base_interest(loan) * delta.days

    assert SimpleLoanCalculator.accrued_interest_to_date(loan, day_of_calculation) == expected_result
