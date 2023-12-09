
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    folders = relationship('Folder', back_populates='user')

class Folder(Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship('User', back_populates='folders')
    files = relationship('File', back_populates='folder')

class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    content = Column(String, nullable=True)  # You might want to adjust the data type
    folder_id = Column(Integer, ForeignKey('folders.id'), nullable=False)

    folder = relationship('Folder', back_populates='files')
