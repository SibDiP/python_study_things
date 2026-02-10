from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///users.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User(username="john_doe", email="john@example.com")
session.add(user)
session.commit()

print("✅ БД создана! Пользователь добавлен!")
print(f"ID: {user.id}")
session.close()



# class UserManager:
#     def __init__(self):
#         self.users = {}
    
#     def add_user(self, username, email):
#         if username in self.users:
#             raise ValueError("User already exists")
#         self.users[username] = email
#         return True
    
#     def get_user(self, username): # return None if nonexist
#         return self.users.get(username)
    
#     def get_user_or_raise(self, username): # raise KeyError if nonexist
#         email = self.get_user(username)
#         if email is None:
#             raise KeyError(f"User '{username}' not found")
#         return email