from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class POS(Base):
    __tablename__ = 'pos'
    name = Column(String, primary_key=True)
    groups = relationship('Group', back_populates='pos')
