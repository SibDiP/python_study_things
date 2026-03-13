from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column( 
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

    def __repr__(self):
        return f"User(id={self.id}), username={self.username}, emai{self.email})"
