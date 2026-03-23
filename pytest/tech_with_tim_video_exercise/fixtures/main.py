from sqlalchemy import create_engine, select, exists
from sqlalchemy.orm import Session, sessionmaker
from models import Base, User
from exceptions import BaseFixturesError, UserAlreadyExistsError, UserNotFoundError

# echo=True - SQL логи
engine = create_engine('sqlite:///users.db', echo=True)
# фабрика. expire_on_commit - не стирает данные объектов полсе commit
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
# создаём таблицы
Base.metadata.create_all(engine)

class UserCRUD:
    # Depency Enjection для удобства тестов.
    def __init__(self,session: Session):
        self.session = session

    def _user_exist(self,email: str) -> bool:
        """Проверить наличие пользователя в БД по уникальному email
        (name не предполагает уникальности)."""
        # Разделение логики:
            # что хотим получить
        stmt = select(exists().where(User.email == email))
            # выполняем запрос
        return self.session.execute(stmt).scalar()
    
    def user_create_or_raise(self, name: str, email: str) -> User:
        """Создать User в БД

        Args:
            name (str): имя пользовтаеля
            email (str): email пользователя

        Raises:
            UserAlreadyExistsError: ошибка при наличии в БД пользователя с переданным email

        Returns:
            User: объект User с актуальными БД параметрами
        """
        if self._user_exist(email):
            raise UserAlreadyExistsError(email)
        
        new_user = User(username=name, email=email)
        # подготовка
        self.session.add(new_user)
        # сохранить в БД
        self.session.commit()
        # подтянуть в объект User все данные (включя генерируемые) из БД.
        self.session.refresh(new_user)
        return new_user
    
    def user_get(self, email: str) -> User | None:
        """Вернуть User с указанным email если он есть в БД.

        Returns:
            User | None: Объект User либо None
        """
        stmt = select(User).where(User.email == email)
        # scalar_one_or_none() - стандарт для Unique поля
        return self.session.execute(stmt).scalar_one_or_none()
    
    def user_update_or_raise(self, email: str, **kwargs) -> User:
        """Обновить данные объекта User в БД

        Args:
            email (str): email пользователя

        Raises:
            UserNotFoundError: ошибка при отсутсвии пользователя с указанным email в БД

        Returns:
            User:  
        """
        user = self.user_get(email)

        if not user:
            raise UserNotFoundError(email)
        
        
        for k,v in kwargs.items():
            if hasattr(user, k):
                setattr(user, k, v)
        
        self.session.commit()
        self.session.refresh(user)
        return user

        
    def user_delite_or_rise(self, email: str) -> bool:
        """Удалить пользователя с указанным email из БД

        Returns:
            bool: 
        
        Raises:
            UserNotFoundError: ошибка при отсутсвии пользователя с указанным email в БД
        """
        user = self.user_get(email)

        if not user:
            raise UserNotFoundError(email)

        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

# Демо
if __name__ == '__main__':
    with SessionLocal() as session:
        crud = UserCRUD(session)

        try:
            user = crud.user_create_or_raise("Jo", "jo@example.com")
            print(f"Создан: {user}")

            updated = crud.user_update_or_raise("jo@example.com", name="Mama")
            print(f"Обновлён: {updated}")

        except (BaseFixturesError) as e:
            print(f"Ошибка логики: {e}")
        except Exception as e:
            print(f"Неопределённая ошибка: {e}")
