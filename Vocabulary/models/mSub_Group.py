from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from Vocabulary.models.mDictionaryBase import DictionaryBase

class Sub_Group(DictionaryBase):
    __tablename__ = 'subgroups'
    name = Column(String, primary_key=True)
    group_id = Column(String, ForeignKey('groups.name'))

    group = relationship('Group', back_populates='subgroups')
    words = relationship('Word', back_populates='subgroup')
