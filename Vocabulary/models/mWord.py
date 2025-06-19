from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from Vocabulary.models.mDictionaryBase import DictionaryBase

class Word(DictionaryBase):
	__tablename__ = 'words'
	id = Column(Integer, primary_key=True)
	word = Column(String)
	translation = Column(String)
	transcription = Column(String)
	weight = Column(Float, default=1.0)
	subgroup_name = Column(String, ForeignKey('subgroups.name'))
	
	subgroup = relationship('Sub_Group', back_populates='words')
