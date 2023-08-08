from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base

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
        + f"WorkoutDay: {self.workout_day}, "\
        + f"WorkoutName: {self.workout_name}, "\
        + f"Reps: {self.reps}, "\
        + f"Sets: {self.sets}, "\
        + f"Weight: {self.weight}"