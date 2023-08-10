from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from models import Name, Exercise, Preference

if __name__ == '__main__':
    engine = create_engine('sqlite:///exercise_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Preference).delete()
    # session.query(Name).delete()

    # all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    #        'Saturday', 'Sunday']
    
    # names = []

    # for _ in range(3):
    #     name = Name(
    #         name='person'
    #     )

    #     session.add(name)
    #     session.commit()

    #     names.append(name)

    # preferences = []

    # for name in names:
    #     for _ in range(random.randint(1,3)):
    #         preference = Preference(
    #             day = random.choice(all_days),
    #             reps = random.randint(6,12),
    #             sets = random.randint(1,4),
    #             weight = random.randint(20, 150),
    #             name_id = name.id
    #         )

    #         session.add(preference)
    #         session.commit()

    #         preferences.append(preference)

    exercises = ['barbell bicep curl',
'bench press',
'rope tricep extension',
'hamstring extension',
'cable flys',
'calf raises',
'overhead press',
'squats',
'bent-over row',
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
