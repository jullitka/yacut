from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Regexp, Optional, URL


class ShortURLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(DataRequired(message='Обязательное поле'),
                    URL(message='Некорректный url'))
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16),
                    Optional(),
                    Regexp(regex=r'^[A-Za-z0-9]+$',
                           message='Присутствуют недопустимые символы!')]
    )
    submit = SubmitField('Создать')
