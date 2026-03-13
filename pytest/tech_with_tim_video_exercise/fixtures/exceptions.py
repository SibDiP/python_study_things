class BaseFixturesError(Exception):
    """Базовое исключение, что б ловить все ошибки приложения"""
    pass

class UserAlreadyExistsError(BaseException):
    """Ошибка: пользователь с таким email уже существует

    Args:
        email (str): email пользователя
    """
    def __init__(self, email: str):
        self.email = email
        self.message = f"Пользователь с email {email} уже существует в БД."
        super().__init__(self.message)

