from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RequestForm(FlaskForm):
    username = StringField(validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Enter GitHub username"})
    submit = SubmitField('Send', render_kw={"class": "btn btn-primary mt-2"})
