from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

from Vocabulary.models.mDictionaryBase import DictionaryBase

class Sub_Group(DictionaryBase):
    __tablename__ = 'subgroups'
    name = Column(String, primary_key=True)
    main_group_id = Column(String, ForeignKey('main_groups.name'))

    # Single date when exam was completed
    exam_completed_at = Column(DateTime, nullable=True)

    main_group = relationship('Group', back_populates='subgroups')
    words = relationship('Word', back_populates='subgroup')
    grades = relationship('Grade', back_populates='subgroup')