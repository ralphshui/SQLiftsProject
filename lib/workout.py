from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base

import click

Base = declarative_base()

class Name(Base):
    __tablename__= 'names'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"{click.style('Name:', fg='green', bold=True)} {self.name}"

class Exercise(Base):
    __tablename__= 'Exercises'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    exercise = Column(String())

    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"{click.style('Exercise:', fg='green', bold=True)} {self.exercise}"

class Preference(Base):
    __tablename__= 'preferences'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    workout_day = Column(String())
    exercise = Column(String())
    reps = Column(Integer())
    sets = Column(Integer())
    weight = Column(Integer())
 
    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"{click.style('Day:', fg='green', bold=True)} {self.workout_day}, "\
        + f"{click.style('Name:', fg='green', bold=True)} {self.exercise}, "\
        + f"{click.style('Reps:', fg='green', bold=True)} {self.reps}, "\
        + f"{click.style('Sets:', fg='green', bold=True)} {self.sets}, "\
        + f"{click.style('Weight:', fg='green', bold=True)} {self.weight}"



