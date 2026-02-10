from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField

class BaseMediaForm(FlaskForm):
    name = StringField("სახელი")
    image = StringField("ფოტოს ლინკი")
    date = IntegerField("გამოშვების წელი")
    genre = StringField("ჟანრი")
    director = StringField("რეჟისორი")
    actors = StringField("მთავარი მსახიობები")
    description = TextAreaField("მოკლე აღწერა")

    save = SubmitField("შენახვა")


class MovieForm(BaseMediaForm):
    pass

class AnimationForm(BaseMediaForm):
    pass

class SerialForm(BaseMediaForm):
    pass

