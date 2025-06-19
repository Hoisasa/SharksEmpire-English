from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from Vocabulary.models.mDictionaryBase import DictionaryBase


class POS(DictionaryBase):
    __tablename__ = 'pos'
    name = Column(String, primary_key=True)
    groups = relationship('Group', back_populates='pos')
