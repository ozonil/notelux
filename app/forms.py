from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from app.models import Info

class InfoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('info', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('enter')

    def validate_title(self, title):
        info = Info.query.filter_by(title=title.data).first()
        if user is not None:
            raise ValidationError("Info already present.")
