import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum
)
from sqlalchemy.orm import relationship

from .meta import Base

class CourseType(enum.Enum):
    compulsory = 1
    optional = 2

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_number = Column(String, nullable=False)
    type = Column(Enum(CourseType), nullable=False)
    # - college
    college_id = Column(Integer, ForeignKey('college.id'))
    college = relationship("College", back_populates="courses")
    # - teacher
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship("Teacher", back_populates="teachers")




