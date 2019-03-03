from flask import render_template,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,CommentForm,PitchForm
from ..models import User,Pitch,Comment
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
        db.session.add(user)
        db.session.commit()
    return render_template("profile/profile.html", user = user)   

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.description = form.description.data

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data
        description = form.description.data
        new_pitch = Pitch(pitch =pitch , description = description)
        new_pitch.save_pitches()
        return redirect(url_for('.index'))
    return render_template('new_pitch.html', pitch_form=form)

@main.route('/comment/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    imishwi =Comment.query.filter_by(pitch_id = id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment = comment , pitch_id=id, user=current_user)
        new_comment.save_comment()
        return redirect(url_for('.new_comment'))
    return render_template('new_comment.html', imishwi=imishwi,comment_form=form)

# @main.route('/view/comment/<int:id>')
# def view_comments(id):
#     '''
#     Function that returs  the comments belonging to a particular pitch
#     '''
#     comments = Comment.get_comments(id)
#     return render_template('view_comments.html',comments = comments, id=id)
