from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

from Vocabulary.models.mDictionaryBase import DictionaryBase


class Grade(DictionaryBase):
	__tablename__ = 'grades'
	
	id = Column(Integer, primary_key=True)
	subgroup_name = Column(String, ForeignKey('subgroups.name'), nullable=False)
	grade = Column(Integer, nullable=True)
	epoch = Column(Integer, nullable=False)
	
	subgroup = relationship('Sub_Group', back_populates='grades')
