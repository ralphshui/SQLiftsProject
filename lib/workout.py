from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String, CHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import click

Base = declarative_base()

class Workout(Base):
    __tablename__= 'workouts'
    __table_args__= (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    workout_name = Column(String())
    reps = Column(Integer())
    sets = Column(Integer())
    weight = Column(Integer())

    def __repr__(self):
        return f"Id: {self.id}, "\
        + f"WorkoutName: {self.workout_name}, "\
        + f"Reps: {self.reps}, "\
        + f"Sets: {self.sets}, "\
        + f"Weight: {self.weight}"

    @click.command()
    @click.option("--workout_name", prompt="Enter the name of workout ", help="The name of the workout")
    @click.option("--sets", prompt="Enter the number of sets ", help="The number of sets per workout")
    @click.option("--reps", prompt="Enter the number of reps ", help="The number of reps per set")
    @click.option("--weight", prompt="Enter the lifting weight (in lbs)", help="The weight you are lifting for the workout")
    def __init__(self, workout_name, reps, sets, weight):
        """asks user to input workout(names, sets, reps, weight)"""
        self.workout_name = workout_name
        self.reps = reps
        self.sets = sets
        self.weight = weight 
        
        engine = create_engine('sqlite:///workouts.db')
        Base.metadata.create_all(engine)

        Session = sessionmaker(engine)
        session = Session()

        session.add(workout_name, sets , reps , weight)
        
        session.commit()
        
        # click.echo(f"Workout: {workout_name}")
        # click.echo(f"Sets: {sets}")
        # click.echo(f"Reps: {reps}")
        # click.echo(f"Weight: {weight}lbs")

# if __name__ == '__main__':
