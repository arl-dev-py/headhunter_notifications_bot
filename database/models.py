from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer


class Base(DeclarativeBase):
    pass


class Vacancies(Base):
    __tablename__ = "vacancies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vac_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
