from flask import Blueprint, render_template, url_for
from flask_login import login_required

event_bp = Blueprint('event', __name__, url_prefix='/event')

@event_bp.route('/create')
@login_required
def create_event():
    return render_template('events/event-creation-update.html', context='static/style/css.css')

@event_bp.route('/details')
def detail():
    return render_template('events/event-details.html')
