from typing import Optional
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class Base(DeclarativeBase):
  pass


class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String(100), unique=True)
  age: Mapped[Optional[int]]  # Optional/nullable column

  def __repr__(self) -> str:
    return (
        f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
    )


engine = create_engine("sqlite:///app.db", echo=False)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


with SessionLocal() as session:
  new_user = User(name="Alice Smith", email="alice@example.com", age=30)
  another_user = User(name="Bob Jones", email="bob@example.com", age=25)

  session.add_all([new_user, another_user])
  session.commit()

with SessionLocal() as session:
  stmt = select(User).where(User.age > 26)
  users = session.scalars(stmt).all()

  for user in users:
    print(user) 