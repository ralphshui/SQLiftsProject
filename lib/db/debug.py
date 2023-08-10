from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Name, Exercise, Preference )

if __name__ == '__main__':

    engine = create_engine('sqlite:///exercise_app.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    name = session.query(Name).first()

    # print(name.name)

    preference = session.query(Preference).first()
    print(preference)