import os
from config import db
from models import Person, Flight, Property
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
