from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')