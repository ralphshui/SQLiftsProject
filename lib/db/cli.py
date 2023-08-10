from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Name, Exercise, Preference, Base

import click

current_user = None

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
@click.option("--confirm", prompt="Are you a new user? [y/n] ", help="Confirms new or current user")
def greeting(confirm):
    """Greeting user to CLI"""
    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    global current_user
    current_user = None
    
    if confirm == 'y':
        add_name = input("Enter your name: ")
        new_name = Name(name = add_name)
        session.add(new_name)
        session.commit()
        current_user = new_name

        click.echo()
        click.echo(f"Hello {click.style(add_name, fg='yellow', bold=True)}, Welcome to {click.style('SQLIFTS', fg='cyan', bold=True)}!")
        click.echo("Your one place to update all your gym workouts. Let's begin planning your exerises!")
        click.echo()
        menu()
    elif confirm == 'n':
        old_name = input("Enter your name: ")
        current_user = session.query(Name).filter(Name.name == old_name).first()
        click.echo()
        if current_user:
            click.echo(f"Welcome back {click.style(old_name, fg='yellow', bold=True)}! Let's continue updating your exerises.")
            click.echo()
            menu()
            
        else:
            click.echo(f"{click.style('Name not found!', fg='red')}")
            click.echo()


def add():
    """asks user to input exercise details(day, reps, sets, weight) after adding by name"""
    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_exercises = [exercise[0] for exercise in session.query(Exercise.exercise).all()]
    add_exercise = input(f"{click.style('Choose an exercise to add by name: ', fg='green', bold=True)}")

    if add_exercise in all_exercises:
        new_day = input(f"{click.style('Enter the day of workout (monday-sunday): ', fg='green', bold=True)}").lower()
        new_reps = input(f"{click.style('Enter the number of reps: ', fg='green', bold=True)}")
        new_sets = input(f"{click.style('Enter the number of sets: ', fg='green', bold=True)}")
        new_weight = input(f"{click.style('Enter the lifting weight (in lbs): ', fg='green', bold=True)}")
        
        workout = Preference(exercise=add_exercise,day=new_day,reps=new_reps,sets=new_sets,weight=new_weight, name_id=current_user.id)
        session.add(workout)
        session.commit()

        click.echo()
        click.echo(f"{rainbow_text('YOUR EXERCISE HAS BEEN SUCCESSFULLY ADDED!!!')}")
        click.echo(f"{click.style('Exercise:', fg='green', bold=True)} {add_exercise}")
        click.echo(f"{click.style('Day:', fg='green', bold=True)} {new_day}")
        click.echo(f"{click.style('Reps:', fg='green', bold=True)} {new_reps}")
        click.echo(f"{click.style('Sets:', fg='green', bold=True)} {new_sets}")
        click.echo(f"{click.style('Weight:', fg='green', bold=True)} {new_weight}lbs")
        click.echo()
    else:
        click.echo(f"{click.style('Exercise not Found! Please refer to list of all exercises (Option #1 in menu)', fg='red')}")
        click.echo()


def all():
    """Show all available workouts from exercise_app.db"""
    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Exercise).delete()

    exercises = ['barbell bicep curl', 
    'bench press',
    'rope tricep extension',
    'hamstring extension',
    'cable flys',
    'calf raises',
    'overhead press',
    'squats',
    'bentover row',
    'deadlift',
    'leg extension',
    'leg press',
    'incline bench press',
    'lat pull down',
    'lateral raises',
    'upright row',
    'shrugs',
    'preacher curl',
    'close grip bench press',
    'pull ups',
    'push ups',
    'hip thrust']
    
    for exercise_name in exercises:
        exercise = Exercise(exercise = exercise_name)
        session.add(exercise)
        session.commit()

    all_exercises = session.query(Exercise).all()
    click.echo()
    click.echo(f"{click.style('**********All Workouts**********', fg='cyan', bold=True)}")
    for exercise in all_exercises:
        click.echo(exercise)
    click.echo()


def current():
    """Shows all current workouts added by user"""
    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    current_workouts=session.query(Preference).filter(Preference.name_id == current_user.id).all()
    click.echo(current_workouts)


def update():
    """filters a specific current workout by name and then allows update"""
    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    current_user_workouts=session.query(Preference).filter(Preference.name_id == current_user.id).all()
    update_workout_id = int(input(f"Enter the {click.style('Id', fg='yellow')} of your workout to update: "))
    update_workout = session.query(Preference).filter(Preference.id == update_workout_id).first()
    workout_found = False

    for workout in current_user_workouts:
        if update_workout_id == workout.id:
            workout_found = True
            click.echo()
            click.echo(update_workout)
            update_input = input(f"What would you like to update ({click.style('day, reps, sets, weight', fg='green')})?: ")

            if update_input.lower() == 'day':
                input_new_day = input(f"Enter new {click.style('day', fg='green')} for {update_workout.exercise}: ")
                update_workout.day = input_new_day
                session.commit()
                click.echo(f"{rainbow_text('WORKOUT DAY HAS BEEN SUCCESSFULLY UPDATED!!!')}")
                click.echo()
                click.echo(update_workout)

            elif update_input.lower() in ('reps', 'rep'):
                input_new_reps = input(f"Enter new {click.style('reps', fg='green')} for {update_workout.exercise}: ")
                update_workout.reps = input_new_reps
                session.commit()
                click.echo(f"{rainbow_text('WORKOUT REPS HAS BEEN SUCCESSFULLY UPDATED!!!')}")
                click.echo()
                click.echo(update_workout)

            elif update_input.lower() in ('sets', 'set'):
                input_new_sets = input(f"Enter new {click.style('sets', fg='green')} for {update_workout.exercise}: ")
                update_workout.sets = input_new_sets
                session.commit()
                click.echo(f"{rainbow_text('WORKOUT SETS HAS BEEN SUCCESSFULLY UPDATED!!!')}")
                click.echo()
                click.echo(update_workout)

            elif update_input.lower() == 'weight':
                input_new_weight = input(f"Enter new {click.style('weight', fg='green')} for {update_workout.exercise}: ")
                update_workout.weight = input_new_weight
                session.commit()
                click.echo(f"{rainbow_text('WORKOUT WEIGHT HAS BEEN SUCCESSFULLY UPDATED!!!')}")
                click.echo(update_workout)
            else:
                click.echo(f"{click.style('Atrribute Not Found! Please type: day, reps, sets, weight', fg='red')}")
    if not workout_found:
        click.echo(f"{click.style('Workout Not Found!', fg='red')}")
        click.echo()


def search():
    """search current workouts by name or day"""
    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    current_user_workouts=session.query(Preference).filter(Preference.name_id == current_user.id).all()
    
    search = input(f"Search by {click.style('name', fg='green')} or {click.style('day', fg='green')}: ")
    
    if search.lower() == 'day':
        workout_found = False
        search_day = input(f"Which {click.style('day', fg='green')} (monday-sunday)? ").lower()

        for workout in current_user_workouts:
            if search_day in workout.day:
                click.echo(workout)
                workout_found = True
        if not workout_found:
            click.echo(f"{click.style(f'No workouts found on {search_day}. Try Again!', fg='red')}")

    elif search.lower() == 'name':
        workout_found = False
        search_name = input("What is the name of the exercise? ").lower()

        for workout in current_user_workouts:
            if search_name in workout.exercise:
                click.echo()
                click.echo(workout)
                workout_found = True
        if not workout_found:
            click.echo(f"{click.style('No workouts found. Try Again!', fg='red')}")

    else:
        click.echo(f"{click.style('Invalid search. Please type day or name', fg='red')}")


@click.option("--delete", prompt="Enter the name of the workout you would like to delete ",
help="deleting workout by name")
def delete(delete):
    """Delete a workout from workouts.db"""
    engine = create_engine('sqlite:///workouts.db')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_workout = session.query(Workout).filter(Workout.workout_name.ilike(delete)).first()
    confirm = click.confirm("Are you sure?")

    if delete_workout:
        if confirm:
            session.delete(delete_workout)
            session.commit()
            click.echo(f"{click.style('Successfully Deleted!', fg='red')}")
        else:
            click.echo(f"{click.style('please return to Commands', fg='magenta')}") 
    else:
        click.echo(f"{click.style('Workout not Found!', fg='magenta')}")


def menu():
    """SQLIFTS interface menu"""
    choice = 0
    while choice !=7:
        click.echo(f"{click.style('**********SQLIFTS Menu**********', fg='cyan', bold=True)}")
        click.echo(f"1# {click.style('View all available workouts', fg='blue')}")
        click.echo(f"2# {click.style('View all current workouts', fg='blue')}")
        click.echo(f"3# {click.style('Add workout', fg='blue')}")
        click.echo(f"4# {click.style('Update current workouts', fg='blue')}")
        click.echo(f"5# {click.style('Delete a workout', fg='blue')}")
        click.echo(f"6# {click.style('Search current workouts by name or day', fg='blue')}")
        click.echo(f"7# {click.style('Quit', fg='red')}")
        click.echo()
        choice = int(input(f"{click.style('Enter your option: ', fg='blue')}"))

        if choice == 1:
            all()
        elif choice == 2:
            current()
        elif choice == 3:
            add()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 6:
            search()
        else:
            exit        

cli.add_command(greeting)

if __name__ == '__main__':
    cli()