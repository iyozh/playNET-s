from wtforms import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class FeedBackForm(Form):
    name = StringField("", validators=[DataRequired()], render_kw={'placeholder': 'Имя'})
    email = StringField("", validators=[DataRequired()], render_kw={'placeholder': "Email"})
    # planet = SelectField(
    #     "",
    #     choices=[
    #         ("mercury", "Меркурий"),
    #         ("venus", "Венера"),
    #         ("mars", "Марс"),
    #         ("jupiter", "Юпитер"),
    #         ("saturn", "Сатурн"),
    #         ("uranus", "Уран"),
    #         ("neptune", "Нептун"),
    #         ("pluto", "Плутон"),
    #     ],
    #     validators=[DataRequired()], render_kw={'placeholder': 'Планета'}
    # )
    message = TextAreaField("", validators=[DataRequired()], render_kw={'placeholder': 'Сообщение'})
