import datetime
import decimal
from oneiro.simple_loan import SimpleLoan


class SimpleLoanCalculator:
    
    def get_daily_base_interest(loan:SimpleLoan) -> decimal:
        return loan.base_rate/365  #refactor to include in leap years

    def daily_base_interest_accrual(loan: SimpleLoan, day_of_calc: datetime) -> decimal:
        delta = day_of_calc - loan.get_start_date()
        return SimpleLoanCalculator.get_daily_base_interest(loan) * delta.days