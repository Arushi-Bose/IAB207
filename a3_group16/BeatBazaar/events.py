from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user
from .forms import EventForm, CommentForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import os
from . import db
from .models import Event, Comment

event_bp = Blueprint('event', __name__, url_prefix='/event')


@event_bp.route('/<id>')
def show(id):
    events = db.session.scalar(db.select(Event).where(Event.id==id))

    # comment form
    form = CommentForm()
    return render_template('events/event-details.html', events=events, form=form)

@event_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_event():
    create = EventForm(CombinedMultiDict((request.form, request.files)))

    if create.is_submitted():
        
        image_path = check_upload_file(create)

        event = Event(
        name = create.event_name.data,
        image = image_path,
        country = create.event_country.data,
        date = create.event_date.data,
        start_time = create.event_start_time.data,
        end_time = create.event_end_time.data,
        description = create.event_description.data,
        venue = create.event_venue.data,
        address = create.event_address.data,
        city = create.event_city.data,
        state = create.event_state.data,
        postcode = create.event_postcode.data,
        number_tickets = create.event_number_tickets.data,
        ticket_price = create.event_ticket_price.data,
        special_ticket = create.event_special_ticket.data
        )
        # adds the inputs to the db session
        db.session.add(event)
        # Commits the inputs to the database
        db.session.commit()

        return redirect(url_for('event.create_event'))
    else:
        return render_template('events/event-creation-update.html', form=create)

def check_upload_file(form):
  #get file data from form  
  fp = form.event_image.data
  filename = fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path = os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path = '/static/image/' + secure_filename(filename)
  #save the file and return the db upload path
  fp.save(upload_path)
  return db_upload_path

@event_bp.route('/details', methods=['GET', 'POST'])
def details():
    return render_template('events/event-details.html')


@event_bp.route('/<id>/comment', methods=['GET', 'POST'])
def comment(id):
    form = CommentForm()

    events = db.session.scalar(db.select(Event).where(Event.id==id))

    if form.validate_on_submit():
        comment = Comment(text=form.text.data, events=events, user=current_user)

        db.session.add(comment)
        db.session.commit()

        flash('Your comment has been added', 'success')
    return redirect(url_for('events/event-details.html', id=id))
