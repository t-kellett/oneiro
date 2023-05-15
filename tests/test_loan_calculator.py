from datetime import datetime
import decimal
import pytest

from oneiro.simple_loan import SimpleLoan
from oneiro.simple_loan_calculator import SimpleLoanCalculator


def test_loan_calculator_gets_correct_loan_days(mock_loan, start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    delta_days = (end - start).days

    assert SimpleLoanCalculator.get_loan_days(mock_loan) == delta_days


def test_loan_calculator_gets_daily_interest_amount(mock_loan):
    delta = mock_loan.get_end_date() - mock_loan.get_start_date()

    expected_result = mock_loan.base_rate/delta.days

    assert SimpleLoanCalculator.get_daily_base_interest(mock_loan) == expected_result


def test_loan_calculation_returns_daily_interest_no_margin(mock_loan):
    day_of_calculation = datetime.strptime('2022-05-01', '%Y-%m-%d')
    delta = day_of_calculation - mock_loan.get_start_date()
    
    expected_result = SimpleLoanCalculator.get_daily_base_interest(mock_loan) * delta.days

    assert SimpleLoanCalculator.accrued_interest_to_date(mock_loan, day_of_calculation) == expected_result


def test_loan_calculator_calculates_total_term_interest(mock_loan):
    expected_result = mock_loan.principal * mock_loan.get_total_interest() * SimpleLoanCalculator.get_loan_days(mock_loan)/365

    assert SimpleLoanCalculator.get_loan_term_interest(mock_loan) == expected_result