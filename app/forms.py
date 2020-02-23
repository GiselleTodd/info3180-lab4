from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Email


class UploadForm(FlaskForm):
    upload = FileField('File Upload',validators=[FileRequired(),FileAllowed(['jpg','png'])])
