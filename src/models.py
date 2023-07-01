import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)
    planets_id = Column(Integer, ForeignKey('planet.id'))

class FavoriteStarship(Base):
    __tablename__ = 'favorite_starship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)
    starship_id = Column(Integer, ForeignKey('starship.id'))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    films = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    homeworld = Column(String(250))
    mass = Column(String(250))
    skin_color = Column(String(250))
    species = Column(String(250))
    starships = Column(String(250))
    vehicles = Column(String(250))
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

    

class Planets(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name  = Column(String(250))
    climate  = Column(String(250))
    diameter  = Column(String(250))
    films  = Column(String(250))
    gravity  = Column(String(250))
    orbital_period  = Column(String(250))
    population  = Column(String(250))
    residents  = Column(String(250))
    rotation_period  = Column(String(250))
    surface_water  = Column(String(250))
    terrain  = Column(String(250))
    url  = Column(String(250))
    

class Starships(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    MGLT = Column(String(250))
    Cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    cost_in_credits = Column(String(250))
    created = Column(String(250))
    crew = Column(String(250))
    edited = Column(String(250))
    hyperdrive_rating = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    name = Column(String(250))
    passengers = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    starship_class = Column(String(250))
    url = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
