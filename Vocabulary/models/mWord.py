from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    translation = Column(String)
    transcription = Column(String)
    weight = Column(Float)
    subgroup_name = Column(String, ForeignKey('subgroups.name'))

    subgroup = relationship('SubGroup', back_populates='words')
