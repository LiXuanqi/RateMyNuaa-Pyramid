from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    overall = Column(Integer)
    attendance = Column(Integer)
    difficulty = Column(Integer)
    grade = Column(Integer)
    test_type = Column(String)
    user_ip = Column(String)
    visible = Column(Integer)

    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="comments")