from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField,BooleanField
from wtforms.validators import Length, Email, InputRequired

class QuizForm(FlaskForm):
    carat = SelectField('carat', choices=[(0, '0'), (1, '1')])
    depth = TextAreaField('depth')
    table = BooleanField('table')
    x = TextAreaField('x')
    y = TextAreaField('y')
    z = TextAreaField('z')

