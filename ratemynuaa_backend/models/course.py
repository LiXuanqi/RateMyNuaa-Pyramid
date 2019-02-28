import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    course_number = Column(String, nullable=False)
    type = Column(String, nullable=False)
    # - college
    college_id = Column(Integer, ForeignKey('colleges.id'))
    college = relationship("College", back_populates="courses")
    # - teacher
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="courses")




