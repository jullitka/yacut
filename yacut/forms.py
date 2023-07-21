from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Regexp, Optional, URL

from .constants import MAX_SHORT_SIZE, REGEX_PATTERN


class ShortURLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(DataRequired(message='Обязательное поле'),
                    URL(message='Некорректный url'))
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=MAX_SHORT_SIZE),
                    Optional(),
                    Regexp(regex=REGEX_PATTERN,
                           message='Присутствуют недопустимые символы!')]
    )
    submit = SubmitField('Создать')
