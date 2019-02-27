from sqlalchemy import (
    Column,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from .meta import Base

class College(Base):
    __tablename__ = 'colleges'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    courses = relationship("Course", back_populates="college")

    teachers = relationship("Teacher", back_populates="college")


