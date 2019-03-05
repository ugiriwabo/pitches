from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User,Pitch,Comment

class PitchForm(FlaskForm):
    pitch =  TextAreaField('Pitch ', validators=[Required()])
    description = TextAreaField('description ', validators=[Required()])
    category = SelectField('Select Category', choices=[('round-table-pitches' ,'Round Table pitches'), ('central-pitches','Central Pitches'),('rough-cut-projects' ,'Rough Cut Projects')])
    submit = SubmitField('Submit')
    

class CommentForm(FlaskForm):
    comment = TextAreaField('username comment', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    description = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
