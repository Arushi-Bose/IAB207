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
    number = StringField("Contact Number", validators=[InputRequired(), Length(min=10, max=10)])
    address = StringField("Residential Address", validators=[InputRequired()])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                Length(min=8, message='%(min)d'),  
                EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class EventForm(FlaskForm):
    event_name=StringField("Event Name", validators=[InputRequired('Enter an event name')])
    event_image = FileField(validators=[FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
    event_country = StringField('Country of Origin', validators=[InputRequired('Enter an event name')])
    event_date = DateField('Event Date', validators=[InputRequired('Enter an event name')])
    event_start_time = StringField('Start Time', validators=[InputRequired('Enter an event name')])
    event_end_time = StringField('End Time', validators=[InputRequired('Enter an event name')])
    event_description = TextAreaField('Description of Event', validators=[InputRequired('Enter an event name')])
    event_venue = StringField('Event Venue')
    event_address = StringField('Address')
    event_city = StringField('City')
    event_state = SelectField('State', choices=[('qld', 'QLD'), ('nsw', 'NSW'), ('act', 'ACT'), ('vic','VIC'), ('sa','SA'), ('tas', 'TAS'), ('wa', 'WA'), ('nt', 'NT')])
    event_postcode = StringField('Postcode')
    event_number_tickets = IntegerField('Number of Tickets', validators=[InputRequired()])
    event_ticket_price = IntegerField('Price ($)', validators=[InputRequired()])
    event_special_ticket = SelectField('Ticket Type', choices=[('vip','VIP'), ('general', 'General')])

    # Submit button
    submit = SubmitField("Create event")

class CommentForm(FlaskForm):
    text=TextAreaField('Comment', [InputRequired()])
    submit= SubmitField('Create Comment')