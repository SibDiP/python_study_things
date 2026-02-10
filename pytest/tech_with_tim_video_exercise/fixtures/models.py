from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import (
    Integer, String, CheckConstraint,
    )

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=False,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(254),
        unique=True,
        nullable=False
    )

    __table_args__ = (
        CheckConstraint('LENGTH(username) <= 50', name='username_maxlen'),
        CheckConstraint('LENGTH(email) <= 254', name='email_maxlen')
    )
