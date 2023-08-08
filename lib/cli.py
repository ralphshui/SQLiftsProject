from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from workout import Workout, Base

import click

def rainbow_text(text):
    rainbow_colors = ["red", "yellow", "green", "blue", "magenta", "cyan"]
    rainbow_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        rainbow_text += click.style(char, fg=color)
    return rainbow_text

@click.group()
def cli():
    pass

@click.command()
@click.option("--name", prompt="Enter your name ", help="The name of the user")
def greeting(name):
    """Greeting user to CLI"""
    click.echo(f"Hello {name}, Welcome to {click.style('SQLIFTS', fg='cyan', bold=True)}!")
    click.echo("Your one place to update all your gym workouts. Let's begin planning your excerises!")



@click.command()
def menu():
    """SQLIFTS interface menu"""
    choice = 0
    while choice !=5:
        click.echo(f"*****{click.style('SQLIFTS', fg='cyan', bold=True)} Menu****")
        click.echo("1# Add new workout")
        click.echo("2# Modify current workouts")
        click.echo("3# View current workouts")
        click.echo("4# Delete a workout")
        click.echo("5# Quit")
        
        choice = int(input('Enter your option: '))

        if choice == 1:
            cli(add)



@click.command()
@click.option("--workout_day", prompt="Enter the day of workout (Monday-Sunday) ", help="The day of workout")
@click.option("--workout_name", prompt="Enter the name of workout ", help="The name of the workout")
@click.option("--reps", prompt="Enter the number of reps ", help="The number of reps per set")
@click.option("--sets", prompt="Enter the number of sets ", help="The number of sets per workout")
@click.option("--weight", prompt="Enter the lifting weight (in lbs)", help="The weight you are lifting for the workout")
def add(workout_day, workout_name, reps, sets, weight):
    """asks user to input workout(name, reps, sets, weight)"""
    click.echo(f"{rainbow_text('YOUR WORKOUT HAS BEEN SUCCESSFULLY ADDED!!!')}")
    click.echo(f"{click.style('Day:', bold=True)} {workout_day}")
    click.echo(f"{click.style('Workout:', bold=True)} {workout_name}")
    click.echo(f"{click.style('Reps:', bold=True)} {reps}")
    click.echo(f"{click.style('Sets:', bold=True)} {sets}")
    click.echo(f"{click.style('Weight:', bold=True)} {weight}lbs")

    engine = create_engine('sqlite:///workouts.db')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    workout = Workout(workout_day=workout_day, workout_name=workout_name, reps=reps, sets=sets, weight=weight)
    session.add(workout)
    session.commit()



@click.command()
def all():
    """Show all workouts from workouts.db"""
    engine = create_engine('sqlite:///workouts.db')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    workouts = session.query(Workout).all()
    
    click.echo(f"{click.style('---All Workouts---', fg='red', bold=True)}")
    for workout in workouts:
        click.echo(workout)



# @click.command()
# def update_workout():
#     """filters a specific workout by name and then allows update"""
#     engine = create_engine('sqlite:///workouts.db')
#     Base.metadata.create_all(bind=engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()


#     session.commit()



@click.command()
@click.option("--delete_workout", prompt="Enter the name of the workout you would like to delete ",
help="deleting workout by name")
def delete(delete_workout):
    """Delete a workout from workouts.db"""
    engine = create_engine('sqlite:///workouts.db')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    workouts = session.query(Workout).all()
    confirm = click.confirm("Are you sure?")

    if confirm:
        for workout in workouts:
            if workout.workout_name.lower() == delete_workout.lower():
                session.delete(delete_workout)
                session.commit()
                click.echo(f"{click.style('Successfully Deleted!', fg='magenta')}")
                break
            else:
                click.echo("Workout not Found!")
    else:
        click.echo("please return to main commands")



cli.add_command(greeting)
cli.add_command(add)
cli.add_command(all)
# cli.add_command(update_workout)
cli.add_command(delete)
cli.add_command(menu)

if __name__ == '__main__':
    cli()