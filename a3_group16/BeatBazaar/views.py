from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/history')
def history():
    return render_template('booking-history.html')

@main_bp.route('/create')
@login_required
def create_event():
    return render_template('events/event-creation-update.html')

@main_bp.route('/details')
def details():
    return render_template('events/event-details.html')