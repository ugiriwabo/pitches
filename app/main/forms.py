from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField,RadioField
from wtforms.validators import Required,Email
from ..models import User

class PitchForm(FlaskForm):
    pitch =  TextAreaField('Pitch ', validators=[Required()])
    description = TextAreaField('description ', validators=[Required()])
    # category_id = SelectField('Select Category', choices=[('Round Table pitches'), ('Genre-specific Round Table pitches'), ('Central pitches'),('Rough Cut Projects')])
    submit = SubmitField('Submit')
    

class CommentForm(FlaskForm):
    username = TextAreaField('username comment', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    description = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')
