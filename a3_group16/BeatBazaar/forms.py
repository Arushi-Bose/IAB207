from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                Length(min=8, message='%(min)d'),  
                EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[InputRequired('Enter an event name')])
    image = FileField('Event Image', validators=[FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
    country = StringField('Country of Origin', validators=[InputRequired('Enter an event name')])
    date = DateField('Event Date', validators=[InputRequired('Enter an event name')])
    start_time = TimeField('Start Time', validators=[InputRequired('Enter an event name')])
    end_time = TimeField('End Time', validators=[InputRequired('Enter an event name')])
    description = TextAreaField('Description of Event', validators=[InputRequired('Enter an event name')])
    venue = StringField('Event Venue')
    address = StringField('Address')
    city = StringField('City')
    state = SelectField('State', choices=[('qld', 'QLD'), ('nsw', 'NSW'), ('act', 'ACT'), ('vic','VIC'), ('sa','SA'), ('tas', 'TAS'), ('wa', 'WA'), ('nt', 'NT')])
    postcode = StringField('Postcode')
    number_tickets = IntegerField('Number of Tickets', validators=[InputRequired(), NumberRange(min=1, max=9999)])
    ticket_price = IntegerField('Price ($)', validators=[InputRequired()])
    special_ticket = SelectField('Ticket Type', validate_choice=[('vip','VIP'), ('general', 'General')])

    # Submit button
    submit = SubmitField("Create Event")