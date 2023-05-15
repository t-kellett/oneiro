import datetime
import decimal
from typing import Protocol


class Loan(Protocol):
    start_date_str: str
    end_date_str: str
    principal: decimal
    currency: str
    base_rate: decimal
    margin: decimal

    def get_start_date(self) -> datetime:
        ...
    
    def get_end_date(self) -> datetime:
        ...

    def get_total_interest(self) -> decimal:
        ...