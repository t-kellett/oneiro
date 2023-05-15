from datetime import datetime
import decimal
import pytest

from oneiro.simple_loan import SimpleLoan

@pytest.fixture
def start_date():
    return '2022-01-01'

@pytest.fixture
def end_date():
    return '2022-12-31'


@pytest.fixture
def mock_loan(monkeypatch, start_date, end_date):
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

    monkeypatch.setattr('oneiro.simple_loan', MockSimpleLoan)

    return SimpleLoan(start_date_str=start_date, end_date_str=end_date, principal=20000,
                  currency='USD', base_rate=0.05, margin=0.02)