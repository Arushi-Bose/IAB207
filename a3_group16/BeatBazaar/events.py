from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_required
from .forms import EventForm
from . import db
from .models import Event

event_bp = Blueprint('event', __name__, url_prefix='/event')

@event_bp.route('/create')
@login_required
def create_event():
    form = EventForm()

    if (form.validate_on_submit()==True):
        event = Event(
        eventname = form.event_name.data,
        eventimage = form.event_image.data,
        eventcountry = form.event_country.data,
        eventdate = form.event_date.data,
        eventstarttime = form.event_start_time.data,
        eventendtime = form.event_end_time.data,
        eventdescription = form.event_description.data,
        eventvenue = form.event_venue.data,
        eventaddress = form.event_address.data,
        eventcity = form.event_city.data,
        eventstate = form.event_state.data,
        eventpostcode = form.event_postcode.data,
        eventnumbertickets = form.event_number_tickets,
        eventticketprice = form.event_ticket_price.data,
        eventspecialticket = form.event_special_ticket.data
        )
        # adds the inputs to the db session
        db.session.add(event)
        # Commits the inputs to the database
        db.session.commit()

        flash('Successfully created the new event')

        return redirect(url_for('event.create'))
    return render_template('events/event-creation-update.html', form=form)

@event_bp.route('/details')
def details():
    return render_template('events/event-details.html')
