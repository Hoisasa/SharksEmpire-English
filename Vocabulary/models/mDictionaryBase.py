from sqlite3 import IntegrityError

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DictionaryBase(Base):
	__abstract__ = True
	
	def add_to_session(self, session):
		session.add(self)
		return self
