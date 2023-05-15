import datetime
import decimal
from oneiro.simple_loan import SimpleLoan


class SimpleLoanCalculator:
    
    def get_loan_days(loan: SimpleLoan) -> int:
        return (loan.get_end_date() - loan.get_start_date()).days

    def get_daily_base_interest(loan:SimpleLoan) -> decimal:
        return loan.base_rate/SimpleLoanCalculator.get_loan_days(loan)

    def accrued_interest_to_date(loan: SimpleLoan, day_of_calc: datetime) -> decimal:
        delta = day_of_calc - loan.get_start_date()
        return SimpleLoanCalculator.get_daily_base_interest(loan) * delta.days