from .db import Base
from sqlalchemy.orm import Mapped,mapped_column

class Book(Base):
 __tablename__ ="book"
 id:Mapped[int] = mapped_column(primary_key=True)
 name:Mapped[str]
 desc:Mapped[str]

