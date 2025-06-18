from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Sub_Group(Base):
    __tablename__ = 'subgroups'
    name = Column(String, primary_key=True)  # globally unique
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='subgroups')
    words = relationship('Word', back_populates='subgroup')
