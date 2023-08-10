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
        return f"Id: {self.id}--"\
        + f"{self.exercise}"


class Preference(Base):
    __tablename__= 'preferences'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer(), primary_key=True)
    day = Column(String())
    reps = Column(Integer())
    sets = Column(Integer())
    weight = Column(Integer())
    
    name_id = Column(Integer(), ForeignKey('names.id'))
    

    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"{self.day}, "\
        + f"{self.reps}, "\
        + f"{self.sets}, "\
        + f"{self.weight}"
