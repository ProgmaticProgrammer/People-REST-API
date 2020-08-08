from datetime import datetime
from marshmallow import fields
from . import db, ma

class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship(
        'Note', # forward reference SQLAlchemy class that Person class will be related to.
        backref='person',
        cascade='all, delete, delete-orphan',# delete all the Note instances associated with it
        single_parent=True,
        order_by='desc(Note.timestamp)'#from newest to oldest
    )

class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'))# 'person' table name here
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        include_relationships = True
        load_instance = True
    notes = fields.Nested('PersonNoteSchema', default=[], many=True)

class PersonNoteSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """
    note_id = fields.Int()
    person_id = fields.Int()
    content = fields.Str()
    timestamp = fields.Str()

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
    person = fields.Nested('NotePersonSchema', default=None)

class NotePersonSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """
    person_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    timestamp = fields.Str()

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