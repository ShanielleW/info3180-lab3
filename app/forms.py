from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, Email


class Contact(form):
    u_name = StringField("Name", validators=[DataRequired()])
    u_email = StringField('E-mail', validators=[DataRequired(), Email()])
    e_subject = StringField('Subject', validators=[DataRequired()])
    e_message = TextAreaField('Message', validators=[DataRequired()])
