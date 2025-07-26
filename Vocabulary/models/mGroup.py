from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from Vocabulary.models.mDictionaryBase import DictionaryBase


class Group(DictionaryBase):
    __tablename__ = 'main_groups'
    name = Column(String, primary_key=True)
    pos_name = Column(String, ForeignKey('pos.name'))

    pos = relationship('POS', back_populates='main_groups')
    subgroups = relationship('Sub_Group', back_populates='main_group')
