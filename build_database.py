import os
from config import db
from models import Person, Flight

# Data to initialize database with
PEOPLE = [
    {"fname": "Doug", "lname": "Farrell"},
    {"fname": "Kent", "lname": "Brockman"},
    {"fname": "Bunny", "lname": "Easter"},
]

FLIGHTS = [
    {"origin": "New York", "destination": "London",  "duration": "415"},
    {"origin": "Shanghai", "destination": "Paris",  "duration": "760"},
    {"origin": "Istanbul", "destination": "Tokyo",  "duration": "700"},
    {"origin": "New York", "destination": "Paris",  "duration": "435"},
    {"origin": "Moscow", "destination": "Paris",  "duration": "245"},
    {"origin": "Lima", "destination": "New York",  "duration": "455"}
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))
    db.session.add(p)

for flight in FLIGHTS:
    f = Flight(origin=flight.get("origin"), destination=flight.get("destination"), duration=flight.get("duration"))
    db.session.add(f)

db.session.commit()
