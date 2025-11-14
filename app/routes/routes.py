from flask import Blueprint, request, render_template, redirect, url_for, flash, send_from_directory
from app.models import *
from app.extenshions import *
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from config import Config
from flask import current_app

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == 'teacher':
        assignments = Assignment.query.filter_by(created_by=current_user.id).all()
    else:
        assignments = Assignment.query.all()
    return render_template("dashboard.html", assignments=assignments)


@main.route('/create_assignment', methods=['GET', 'POST'])
@login_required
def create_assignment():
    if current_user.role != 'teacher':
        flash('Only Teacher Were Create assignments', "danger")
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        assignment = Assignment(title=title, description=description, due_date=due_date, created_by=current_user.id)
        db.session.add(assignment)
        db.session.commit()
        flash("Assignment were created Successfully", "danger")
        return redirect(url_for('main.dashboard'))
    return render_template('create_assignment.html')


@main.route("/submit/<int:assignment_id>", methods = ['GET', 'POST'])
@login_required
def submit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            submission = Submission(
                file_name = filename,
                assignment_id = assignment.id,
                student_id = current_user.id
            )
            db.session.add(submission)
            db.session.commit()
            flash('Assignment Submited Successfully', 'info')
            return redirect(url_for('main.dashboard'))
    return render_template('submit_assignment.html', assignment=assignment)


@main.route('/submissions/<int:assignment_id>')
@login_required
def view_submissions(assignment_id):
    if current_user.role != 'teacher':
        flash('Access denied.')
        return redirect(url_for('main.dashboard'))
    submissions = Submission.query.filter_by(assignment_id=assignment_id).all()
    return render_template('submissions.html', submissions=submissions)