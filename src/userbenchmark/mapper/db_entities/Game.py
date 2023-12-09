from sqlalchemy import Column, Integer, String

from ..BaseSQLAlchemy import Base

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    key = Column(Integer, nullable=False)