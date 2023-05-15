from dataclasses import dataclass, field
from datetime import datetime
import decimal


@dataclass
class SimpleLoan:
    start_date_str: str
    end_date_str: str
    principal: decimal
    currency: str
    base_rate: decimal
    margin: decimal

    def get_start_date(self):
        return datetime.strptime(self.start_date_str, '%Y-%m-%d')
    
    def get_end_date(self):
        return datetime.strptime(self.end_date_str, '%Y-%m-%d')

    def get_total_interest(self) -> decimal:
        return self.base_rate + self.margin
    