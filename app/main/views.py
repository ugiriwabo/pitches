from flask import render_template,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,CommentForm,PitchForm
from ..models import User,Pitch,Comment,PitchCategory
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best pitches Website Online'
    all_pitches = Pitch.get_all_pitches()
    return render_template('index.html', title = title, all_pitches=all_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)   

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        # pitch = form.pitch.data
        description = form.description.data

        new_pitch = Pitch(description = description, user_id=current_user)
        # new_pitch.save_pitches()
        return redirect(url_for('main.index'))
        db.session.add(new_pitch)
        db.session.commit()
    
    
    return render_template('new_pitch.html', pitch_form=form)

@main.route('/new', methods=['GET', 'POST'])
@login_required
def new_comment():
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        username  = comment_form.username.data
        
        new_comment = Comment(username=username, user_id=current_user.id)
        new_comment.save_comment()
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', comment_form=comment_form)