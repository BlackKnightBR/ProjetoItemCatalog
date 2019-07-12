# The sys module provides a number of functions and variables that can be
# used to manipulate different parts of the Python run-time environment.
import sys

# Importing classes
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

# Declarative base, used in the configuration and class code.
from sqlalchemy.ext.declarative import declarative_base

# Relationship, used for foreign key relationships.
from sqlalchemy.orm import relationship

# Used for configuration at the end of file
from sqlalchemy import create_engine

# Instance of the declarative_base we just imported.
# The declarative_base will let SQLAlchemy know that our classes
# are special SQLAlchemy classes that correspond to tables in our database.
Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key = True)
    email = Column(String(80), unique = True, nullable = False)
    password = Column(String(6), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'email': self.email,
        }


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'user_id': self.user_id,
        }


class CategoryItem(Base):
    __tablename__= 'category_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(350), nullable=False)
    picture = Column(String(350), nullable=False)
    dateAdd= Column(DateTime, default=func.now())
    categories_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'picture': self.picture,
            'dateAdd': self.dateAdd,
            'user_id': self.user_id,
        }

######### END of file ###########

#Instance of our class create_engine pointing the database we will use.
#The create_engine will create a new file similary to a more robust database.
engine = create_engine(
'sqlite:///weaponsGuide.db')

#Add the classes as new tables in our database.
Base.metadata.create_all(engine)
