from oneiro.loan_proto import Loan


class Transactions:
    def __init__(self) -> None:
        self.history = {}

    def add_loan(self, loan: Loan) -> int:
        loan_id = id(loan)
        self.history[loan_id] = loan
        return loan_id