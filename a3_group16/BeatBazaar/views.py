from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Event
from .models import Bookings
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    events = db.session.scalars(db.select(Event)).all()
    return render_template('index.html', events=events)

@main_bp.route('/filter/<country>')
def filter(country):
        events = db.session.scalars(db.select(Event).where(Event.country.like(country)))
        return render_template('index.html', events=events)

@main_bp.route('/history')
@login_required
def history():
    bookings = db.session.scalars(db.select(Bookings).where(Bookings.user_id==current_user.id))
    return render_template('booking-history.html', bookings=bookings)