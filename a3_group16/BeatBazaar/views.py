from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .models import Event
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

@main_bp.route('/history/<id>')
@login_required
def history(id):

    event = Event.query.get(id)
    bookings = event.bookings
    return render_template('booking-history.html', bookings=bookings)
