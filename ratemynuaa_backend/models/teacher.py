from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey)
from sqlalchemy.orm import relationship

from .meta import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    courses = relationship("Course", back_populates="teacher")

    college_id = Column(Integer, ForeignKey('college.id'))
    college = relationship("College", back_populates="teachers")

