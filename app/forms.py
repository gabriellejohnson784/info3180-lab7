# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, ValidationError
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired
import os

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    def validate_poster(form, field):
        if not field.data:
            raise ValidationError('Poster is required.')
        filename = field.data.filename
        if not filename.endswith(('.png', '.jpg', '.jpeg')):
            raise ValidationError('Only images .png, .jpg, .jpeg allowed !')

    poster = FileField('Poster', validators=[validate_poster, FileAllowed(['jpg', 'png'], 'Images only!')])

