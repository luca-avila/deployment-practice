from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Counter(Base):
    __tablename__ = "counters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    times_clicked: Mapped[int] = mapped_column(Integer, default=0, nullable=False)