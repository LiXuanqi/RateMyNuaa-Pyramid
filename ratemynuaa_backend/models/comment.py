from sqlalchemy import (
    Column,
    Index,
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
    # - test_type
    # - course_id
    # - user_ip
    # - visible