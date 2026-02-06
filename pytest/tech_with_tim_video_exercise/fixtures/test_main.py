import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()

def test_adds_user_successfully(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com")
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_raises_error_on_duplicate_username(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")

def test_raises_error_on_getting_non_exist_user(user_manager):
    user_name = "john_doe"
    with pytest.raises(KeyError, match=f"User '{user_name}' not found"):
        user_manager.get_user_or_raise(user_name)
        