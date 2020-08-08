"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Property, PropertySchema


def read_all():
    """
    This function responds to a request for /api/property
    with the complete lists of property

    :return:        json string of list of property
    """
    # Create the list of people from our data
    properties = Property.query.with_entities(Property.property_id,
                                              Property.title, 
                                              Property.img_url, 
                                              Property.price_formatted, 
                                              Property.bedroom_number, 
                                              Property.bathroom_number, 
                                              Property.summary).order_by(Property.property_id).all()

    # Serialize the data for the response
    property_schema = PropertySchema(many=True)
    data = property_schema.dump(properties)
    return data

