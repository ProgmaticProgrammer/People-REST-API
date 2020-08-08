from datetime import datetime
from config import db, ma


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True


class Flight(db.Model):
    __tablename__ = "flight"
    flight_id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Property(db.Model):
    __tablename__ = "property"
    property_id = db.Column(db.Integer, primary_key=True)
    center_lat = db.Column(db.Numeric, nullable=False)
    center_lon = db.Column(db.Numeric, nullable=False)
    long_title = db.Column(db.String, nullable=False)
    place_name = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    thumb_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    img_width = db.Column(db.Integer)
    img_height = db.Column(db.Integer)
    price_formatted = db.Column(db.String, nullable=False)
    bedroom_number = db.Column(db.Integer, nullable=False)
    bathroom_number = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String)

class PropertySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Property
        load_instance = True