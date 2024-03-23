import unittest
from unittest.mock import patch, MagicMock
from db.models import Customer
from ..crud import (
    list_users,
    create_user,
    get_user,
    get_user_by_name,
    get_user_by_email,
    update_user,
    delete_user,
    delete_user_by_name,
    delete_user_by_email
)

class TestUserFunctions(unittest.TestCase):

    def test_list_users(self):
        # Mocking the session and query
        with patch('db.session.use_session') as mock_session:
            mock_query = MagicMock()
            mock_session.return_value.__enter__.return_value.query.return_value.all.return_value = [
                Customer(id="988350d9-2018-4fe2-9dd4-222daf692ab5", full_name="John Doe", email="john@example.com"),
                Customer(id="3c5672d1-a2fe-483a-a38c-a184b803b688", full_name="Jane Doe", email="jane@example.com")
            ]
            result = list_users()
            self.assertEqual(len(result), 2)

    def test_create_user(self):
        with patch('db.session.use_session') as mock_session:
            mock_add = MagicMock()
            mock_commit = MagicMock()
            mock_session.return_value.__enter__.return_value.add = mock_add
            mock_session.return_value.__enter__.return_value.commit = mock_commit
            user = create_user("John Doe", "john@example.com")
            self.assertIsInstance(user, Customer)

    def test_get_user(self):
        with patch('db.session.use_session') as mock_session:
            mock_query = MagicMock()
            mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = Customer(id=1, full_name="John Doe", email="john@example.com")
            user = get_user("988350d9-2018-4fe2-9dd4-222daf692ab5")
            self.assertIsInstance(user, Customer)

    @patch('db.session.use_session', return_value=MockSession())
    def test_get_user_by_name(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, full_name="John Doe", email="john@example.com")
        user = get_user_by_name("John Doe")
        self.assertIsNotNone(user)

    @patch('db.session.use_session', return_value=MockSession())
    def test_get_user_by_email(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, full_name="John Doe", email="john@example.com")
        user = get_user_by_email("john@example.com")
        self.assertIsNotNone(user)

    @patch('db.session.use_session', return_value=MockSession())
    def test_update_user(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, full_name="John Doe", email="john@example.com")
        
        # Mocking the session and commit
        mock_commit = MagicMock()
        mock_session = MagicMock(commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session
        
        user = update_user(1, "Jane Doe", "jane@example.com")
        self.assertIsNotNone(user)

    @patch('db.session.use_session', return_value=MockSession())
    def test_delete_user(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, full_name="John Doe", email="john@example.com")
        
        # Mocking the session and delete
        mock_delete = MagicMock()
        mock_commit = MagicMock()
        mock_session = MagicMock(delete=mock_delete, commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session

        result = delete_user(1)
        self.assertTrue(result)

    @patch('db.session.use_session', return_value=MockSession())
    def test_delete_user_by_name(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, full_name="John Doe", email="john@example.com")
        
        # Mocking the session and delete
        mock_delete = MagicMock()
        mock_commit = MagicMock()
        mock_session = MagicMock(delete=mock_delete, commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session

        result = delete_user_by_name("John Doe")
        self.assertTrue(result)

    @patch('db.session.use_session', return_value=MockSession())
    def test_delete_user_by_email(self, mock_use_session):
        # Mocking the session and query
        mock_query = MagicMock()
        mock_use_session.return_value.__enter__.return_value.query.return_value.filter.return_value.first.return_value = MagicMock(id=1, full_name="John Doe", email="john@example.com")
        
        # Mocking the session and delete
        mock_delete = MagicMock()
        mock_commit = MagicMock()
        mock_session = MagicMock(delete=mock_delete, commit=mock_commit)
        mock_use_session.return_value.__enter__.return_value = mock_session

        result = delete_user_by_email("john@example.com")
        self.assertTrue(result)

    # Similarly, you can write tests for other functions like get_user_by_name, get_user_by_email, update_user, delete_user, delete_user_by_name, delete_user_by_email

if __name__ == '__main__':
    unittest.main()
