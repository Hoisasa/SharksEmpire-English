from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import CheckConstraint

from Vocabulary.models.mDictionaryBase import DictionaryBase

class Word(DictionaryBase):
	__tablename__ = 'words'
	id = Column(Integer, primary_key=True)
	word = Column(String)
	translation = Column(String)
	transcription = Column(String)
	weight = Column(Float, default=0.0)
	subgroup_name = Column(String, ForeignKey('subgroups.name'))
	
	subgroup = relationship('Sub_Group', back_populates='words')
	
	__table_args__ = (CheckConstraint('weight >= 0.0 AND weight <= 1.0', name='weight_between_0_and_1'),)
