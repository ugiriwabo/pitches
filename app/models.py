from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
# from datetime import datetime 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches=db.relationship('Pitch',backref='user',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

    
class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")

    def save_pitches(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Pitch.query.all()
    
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    Comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    username =  db.Column(db.String)
    votes= db.Column(db.Integer)
    def save_comment(self):
            '''
            Function that saves comments
            '''
            db.session.add(self)
            db.session.commit()
   
    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments

class PitchCategory(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='pitch_categories'

    id = db.Column(db.Integer, primary_key=True)
    name_of_category = db.Column(db.String(255))
    category_description = db.Column(db.String(255))

class Profile(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='pitch_profile'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def save_profile(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_profile(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Pitch.query.all()