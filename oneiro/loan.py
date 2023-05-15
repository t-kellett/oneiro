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
    