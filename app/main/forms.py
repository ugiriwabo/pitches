from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

class CommentForm(FlaskForm):
    username = TextAreaField('username comment', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    content = TextAreaField('pitch content', validators=[Required()])
    submit = SubmitField('Submit')