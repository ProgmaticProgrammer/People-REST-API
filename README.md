# People-REST-API
REST API providing access to a collection of people with CRUD access to an individual person

With the Connexion module and some additional configuration work, a useful documentation and interactive system 
can be put in place, making your API a much more enjoyable experience for your users to interface with and understand.

HOW_TO: Flask and VSCode
https://code.visualstudio.com/docs/python/tutorial-flask

FIX: ModelSchema issue

# flask-marshmallow>=0.12.0 (recommended)
https://github.com/marshmallow-code/flask-marshmallow/blob/dev/CHANGELOG.rst#0120-2020-04-26
https://marshmallow-sqlalchemy.readthedocs.io/en/latest/changelog.html#id7

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True

FIX: SQLITE uri issue, should be three /
