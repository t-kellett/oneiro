import datetime
import decimal
from oneiro.simple_loan import SimpleLoan


class SimpleLoanCalculator:
    
    def daily_base_interest_accrual(loan: SimpleLoan, day_of_calc: datetime) -> decimal:
        delta = day_of_calc - loan.get_start_date()
        return loan.base_rate/delta.days