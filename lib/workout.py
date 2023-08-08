from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base

import click

Base = declarative_base()

class Workout(Base):
    __tablename__= 'workouts'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    workout_day = Column(String())
    workout_name = Column(String())
    reps = Column(Integer())
    sets = Column(Integer())
    weight = Column(Integer())

    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"{click.style('Day:', fg='green', bold=True)} {self.workout_day}, "\
        + f"{click.style('Name:', fg='green', bold=True)} {self.workout_name}, "\
        + f"{click.style('Reps:', fg='green', bold=True)} {self.reps}, "\
        + f"{click.style('Sets:', fg='green', bold=True)} {self.sets}, "\
        + f"{click.style('Weight:', fg='green', bold=True)} {self.weight}"