import os
from config import db
from models import Person, Flight
import csv

# Delete database file if it exists currently
if os.path.exists("data.db"):
    os.remove("data.db")

# Create the database
db.create_all()

# https://realpython.com/python-csv/
with open('people.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for first_name, last_name in reader:
        people = Person(fname=first_name, lname=last_name)
        db.session.add(people)

with open('flights.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)

db.session.commit()
