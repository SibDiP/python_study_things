import pytest
from main import UserCRUD
from exceptions import BaseFixturesError, UserAlreadyExistsError, UserNotFoundError
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def user_CRUD():
    """Creates a fresh instance of UserCRUD before each test."""
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    return UserCRUD(SessionLocal)

def test_adds_user_successfully(user_CRUD):
    assert user_CRUD.user_create_or_raise("john_doe", "john@example.com")
    assert user_CRUD.user_get("john@example.com") == 











def test_raises_error_on_duplicate_username(user_CRUD):
    user_CRUD.user_create_or_raise("john_doe", "john@example.com")
    with pytest.raises(UserAlreadyExistsError):
        user_CRUD.user_create_or_raise("john_doe", "another@example.com")

def test_raises_error_on_getting_non_exist_user(user_CRUD):
    user_name = "john_doe"
    with pytest.raises(KeyError, match=f"User '{user_name}' not found"):
        user_CRUD.get_user_or_raise(user_name)
        