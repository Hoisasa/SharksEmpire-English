from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pos_name = Column(String, ForeignKey('pos.name'))

    pos = relationship('POS', back_populates='groups')
    subgroups = relationship('SubGroup', back_populates='group')
