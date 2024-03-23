import unittest
from unittest.mock import MagicMock, patch
from ..crud import (
    list_loan,
    create_loan,
    get_loan,
    update_loan,
    delete_loan
)

class MockSession:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class TestLoanFunctions(unittest.TestCase):

    @patch('db.session.use_session', return_value=MockSession())
    def test_list_loan(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.all.return_value = [
            MagicMock(__json__=MagicMock(return_value={"id": 1, "amount": 1000, "customer_id": "123"})),
            MagicMock(__json__=MagicMock(return_value={"id": 2, "amount": 1500, "customer_id": "456"}))
        ]
        result = list_loan()
        self.assertEqual(len(result), 2)

    @patch('db.session.use_session', return_value=MockSession())
    def test_create_loan(self, mock_use_session):
        # Mocking the session and add method
        mock_add = MagicMock()
        mock_commit = MagicMock()
        mock_session = MagicMock(add=mock_add, commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session
        loan = create_loan(1000, "123")
        self.assertIsNotNone(loan)

    @patch('db.session.use_session', return_value=MockSession())
    def test_get_loan(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, amount=1000, customer_id="123")
        loan = get_loan(1)
        self.assertIsNotNone(loan)

    @patch('db.session.use_session', return_value=MockSession())
    def test_update_loan(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, amount=1000, customer_id="123")
        
        # Mocking the session and commit
        mock_commit = MagicMock()
        mock_session = MagicMock(commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session
        
        loan = update_loan(1, 1500)
        self.assertIsNotNone(loan)

    @patch('db.session.use_session', return_value=MockSession())
    def test_delete_loan(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, amount=1000, customer_id="123")
        
        # Mocking the session and delete
        mock_delete = MagicMock()
        mock_commit = MagicMock()
        mock_session = MagicMock(delete=mock_delete, commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session

        delete_loan(1)

if __name__ == '__main__':
    unittest.main()
