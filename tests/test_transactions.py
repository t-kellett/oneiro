from oneiro.transactions import Transactions


def test_transactions_store_loans_with(mock_loan):
    transactions = Transactions()
    loan1, loan2, loan3, loan4 = mock_loan, mock_loan, mock_loan, mock_loan

    loan2.currency = 'GBP'
    loan3.currency = 'EUR'
    loan2.currency = 'JPY'

    loan_id1 = transactions.add_loan(loan1)
    loan_id2 = transactions.add_loan(loan2)
    loan_id3 = transactions.add_loan(loan3)
    loan_id4 = transactions.add_loan(loan4)

    assert transactions.history[loan_id1] == loan1
    assert transactions.history[loan_id2] == loan1
    assert transactions.history[loan_id3] == loan1
    assert transactions.history[loan_id4] == loan1
    