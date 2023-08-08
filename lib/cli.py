from sqlalchemy import Column, Integer, String, CHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Workout import workouts

import click

# Base = declarative_base()

def rainbow_text(text):
    rainbow_colors = ["red", "yellow", "green", "blue", "magenta", "cyan"]
    rainbow_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        rainbow_text += click.style(char, fg=color)
    return rainbow_text

@click.group()
def mycommands():
    pass

@click.command()
@click.option("--name", prompt="Enter your name ", help="The name of the user")
def greeting(name):
    """Greeting user to CLI"""
    click.echo(f"Hello {name}, Welcome to {rainbow_text('SQLIFTS')}!")
    click.echo("Your one place to update all your gym workouts. Let's begin planning your excerises!")

@click.command()
@click.option("--workout_name", prompt="Enter the name of workout ", help="The name of the workout")
@click.option("--sets", prompt="Enter the number of sets ", help="The number of sets per workout")
@click.option("--reps", prompt="Enter the number of reps ", help="The number of reps per set")
@click.option("--weight", prompt="Enter the lifting weight (in lbs)", help="The weight you are lifting for the workout")
# @click.argument('workout_name', 'sets', 'reps', 'weight')
def add_workout(workout_name, sets, reps, weight):
    """Asks user to input workout(names, sets, reps, weight)"""
    click.echo(f"Workout: {workout_name}")
    click.echo(f"Sets: {sets}")
    click.echo(f"Reps: {reps}")
    click.echo(f"Weight: {weight}lbs")

# @click.command()
# def all_workouts():
#     return session.query().all()

# @click.command()
# @click.option("--delete_workout", prompt="Enter the name of workout you would like to delete ", help="deleting workout by name")
# def delete_workout(delete_workout):
#     session.delete(delete_workout)
#     session.commit()

@click.command()
def menu():
    """SQLIFTS interface menu"""
    choice = 0
    while choice !=5:
        click.echo(f"*****{rainbow_text('SQLIFTS')} Menu****")
        click.echo("1# Add new workout")
        click.echo("2# Modify current workouts")
        click.echo("3# View current workouts")
        click.echo("4# Delete a workout")
        click.echo("5# Quit")
        
        choice = int(input('Enter your option: '))

        if choice == 1:
            mycommands(add_workout)

mycommands.add_command(greeting)
mycommands.add_command(add_workout)
# mycommands.add_command(all_workouts)
# mycommands.add_command(modify_workout)
# mycommands.add_command(delete_workout)
mycommands.add_command(menu)

if __name__ == '__main__':
    mycommands()