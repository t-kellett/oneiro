from dataclasses import dataclass
import decimal


@dataclass
class SimpleLoan:
    start_date: str
    end_date: str
    principal: decimal
    currency: str
    base_rate: decimal
    margin: decimal

    def get_total_interest(self) -> decimal:
        return self.base_rate + self.margin
    