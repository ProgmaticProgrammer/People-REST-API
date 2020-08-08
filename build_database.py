import os
from datetime import datetime
from config import db
from models import Person, Note, Property
import csv

# Delete database file if it exists currently
if os.path.exists("data.db"):
    os.remove("data.db")

# Create the database
db.create_all()


# From in file list
# Data to initialize database with
PEOPLE = [
    {
        "fname": "Doug",
        "lname": "Farrell",
        "notes": [
            ("Cool, a mini-blogging application!", "2019-01-06 22:17:54"),
            ("This could be useful", "2019-01-08 22:17:54"),
            ("Well, sort of useful", "2019-03-06 22:17:54"),
        ],
    },
    {
        "fname": "Kent",
        "lname": "Brockman",
        "notes": [
            (
                "I'm going to make really profound observations",
                "2019-01-07 22:17:54",
            ),
            (
                "Maybe they'll be more obvious than I thought",
                "2019-02-06 22:17:54",
            ),
        ],
    },
    {
        "fname": "Bunny",
        "lname": "Easter",
        "notes": [
            ("Has anyone seen my Easter eggs?", "2019-01-07 22:47:54"),
            ("I'm really late delivering these!", "2019-04-06 22:17:54"),
        ],
    },
]

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))

    # Add the notes for the person
    for note in person.get("notes"):
        content, timestamp = note
        p.notes.append(
            Note(
                content=content,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )
    db.session.add(p)

# From csv file
# https://realpython.com/python-csv/
with open('properties.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for center_lat,center_lon,long_title,place_name,title,thumb_url,img_url,img_width,img_height,price_formatted,bedroom_number,bathroom_number,summary in reader:
        property = Property(center_lat=center_lat,
                            center_lon=center_lon,
                            long_title=long_title,
                            place_name=place_name,
                            title=title,
                            thumb_url=thumb_url,
                            img_url=img_url,
                            img_width=img_width,
                            img_height=img_height,
                            price_formatted=price_formatted,
                            bedroom_number=bedroom_number,
                            bathroom_number=bathroom_number,
                            summary=summary)
        db.session.add(property)

db.session.commit()
