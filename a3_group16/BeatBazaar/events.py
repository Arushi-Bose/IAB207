from flask import Blueprint, render_template, url_for
from flask_login import login_required
from .forms import EventForm

event_bp = Blueprint('event', __name__, url_prefix='/event')

@event_bp.route('/create')
@login_required
def create_event():
    form = EventForm()
    return render_template('event/event-creation-update.html', form=form)

@event_bp.route('/details')
def detail():
    return render_template('event/event-details.html')
