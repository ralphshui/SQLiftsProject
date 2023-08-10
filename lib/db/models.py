from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

class Name(Base):
    __tablename__= 'names'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"{self.name}"

    preferences = relationship('Preference', backref=backref('preference'))

class Exercise(Base):
    __tablename__= 'Exercises'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    exercise = Column(String())
    
    def __repr__(self):
        return f"\033[97mId-{self.id}:\033[0m "\
        + f"\033[92m{self.exercise}\033[0m"


class Preference(Base):
    __tablename__= 'preferences'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    exercise = Column(String())
    day = Column(String())
    reps = Column(Integer())
    sets = Column(Integer())
    weight = Column(Integer())
    
    name_id = Column(Integer(), ForeignKey('names.id'))
    

    def __repr__(self):
        return f"\033[93mId\033[0m: {self.id}, "\
        + f"\033[92mExercise\033[0m: {self.exercise}, "\
        + f"\033[92mDay\033[0m: {self.day}, "\
        + f"\033[92mReps\033[0m: {self.reps}, "\
        + f"\033[92mSets\033[0m: {self.sets}, "\
        + f"\033[92mWeight\033[0m(lbs): {self.weight}\n"

