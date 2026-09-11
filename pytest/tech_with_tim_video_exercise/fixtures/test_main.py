import pytest
from sqlalchemy import create_engine
from models import Base, User
from main import UserCRUD
from exceptions import BaseFixturesError, UserAlreadyExistsError, UserNotFoundError
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def db_session():
    test_engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=test_engine)
    TestSession = sessionmaker(bind=test_engine, expire_on_commit=False)
    session = TestSession()
    
    yield session

    session.close()

@pytest.fixture
def user_crud(db_session):
    """Свежая БД в памяти для каждого теста"""
    return UserCRUD(db_session)

@pytest.fixture
def test_user(db_session):
    """Создать тестового пользователя"""
    name = "John"
    email = "JD@mail.com"
    test_user = User(name, email)

    db_session.add(test_user)
    db_session.commit()
    db_session.refresh(test_user)
    return test_user

# тест на существование

# тест на создание

# +возвращение ошибки при создании при наличии дубликата

# +получение юзера

# +обновить данные юзера

# обновить данные юзера - ошибка отсутсвия пользователя

# +удалить пользователя

# удалить пользователя - ошибка при отсутсвии пользователя

































# def test_raises_error_on_duplicate_username(user_CRUD):
#     user_CRUD.user_create_or_raise("john_doe", "john@example.com")
#     with pytest.raises(UserAlreadyExistsError):
#         user_CRUD.user_create_or_raise("john_doe", "another@example.com")

# def test_raises_error_on_getting_non_exist_user(user_CRUD):
#     user_name = "john_doe"
#     with pytest.raises(KeyError, match=f"User '{user_name}' not found"):
#         user_CRUD.get_user_or_raise(user_name)
        