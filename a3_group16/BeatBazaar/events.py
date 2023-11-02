from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user
from .forms import EventForm, BookingForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import os
from . import db
from .models import Event, Comment, Bookings
from random import randint

event_bp = Blueprint('event', __name__, url_prefix='/event')


@event_bp.route('/<id>', methods=['GET', 'POST'])
def show(id):
    form = BookingForm()
    if form.is_submitted():
        print("book button pressed")
        return redirect(url_for('event.purchase', id=id))
    
    events = db.session.scalar(db.select(Event).where(Event.id==id))
    comments = db.session.scalars(db.select(Comment).where(Comment.events_id==id))
    return render_template('events/event-details.html', events=events, comments=comments, form=form)

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
        special_ticket = create.event_special_ticket.data,
        status = create.event_status.data
        )
        # adds the inputs to the db session
        db.session.add(event)
        # Commits the inputs to the database
        db.session.commit()

        return redirect(url_for('main.index'))
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
  db_upload_path = '/static/img/' + secure_filename(filename)
  #save the file and return the db upload path
  fp.save(upload_path)
  return db_upload_path


@event_bp.route('/<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):

    if request.method == 'POST':
        comment = request.form.get('comment')
    if (request.form.get('submit')):
        comment = Comment(text=comment, events_id=id, user_id=current_user.id)

        db.session.add(comment)
        db.session.commit()

        flash('Your comment has been added', 'success')
    return redirect(url_for('event.show', id=id))

@event_bp.route('/<id>/purchase', methods=['GET', 'POST'])
@login_required
def purchase(id):
    print("purchase hit")
    if request.method == 'POST':
        return None
    event = db.session.scalar(db.select(Event).where(Event.id==id))

    booking = Bookings(booking_number=randint(50000,1000000), user_id=current_user.id)
    db.session.add(booking)
    db.session.commit()
    flash('Your tickets have been successfully purchased for event: {}. Your order number is: {}'.format(event.name, booking.booking_number))
    return redirect(url_for('main.index'))
