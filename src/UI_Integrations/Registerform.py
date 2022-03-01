from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import  InputRequired,Length

class registerform(FlaskForm):
    username = StringField('Username',validators=[InputRequired(),Length(min=3,max=10)])
    password = StringField('Password',validators=[InputRequired(),Length(min=3,max=10)])


