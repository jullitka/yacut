from datetime import datetime
from random import choice

from flask import url_for

from . import db
from .error_handlers import InvalidAPIUsage
from .constants import (ALLOWED_SYMBOLS, DEFAULT_SHORT_SIZE, MAX_ORIGINAL_SIZE,
                        MAX_SHORT_SIZE, NUMBER_OF_ATTEMPTS)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_SIZE), nullable=False)
    short = db.Column(db.String(MAX_SHORT_SIZE), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Возвращает словарь с оригинальной и короткой ссылкой"""
        return dict(
            url=self.original,
            short_link=url_for('redirection', short=self.short, _external=True)
        )

    def add_to_db(self):
        """Добавляет объект в базу данных"""
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def is_short_id(cls, short_id):
        """Взвращает объект по short_id, если он существует"""
        return cls.query.filter_by(short=short_id).first()

    @staticmethod
    def generate_random_short_id(short_size=DEFAULT_SHORT_SIZE,
                                 allowed_symbols=ALLOWED_SYMBOLS):
        """Возвращает случайно сгенерированный short_id указанной длины"""
        return ''.join((choice(allowed_symbols) for _ in range(short_size)))

    @classmethod
    def get_unique_random_short_id(cls, short_size=DEFAULT_SHORT_SIZE,
                                   attempts=NUMBER_OF_ATTEMPTS):
        """Возвращает уникальный  случайный short_id указанной длины"""
        for _ in range(attempts):
            short_id = cls.generate_random_short_id(short_size)
            if not cls.is_short_id(short_id):
                return short_id
        raise InvalidAPIUsage('Невозможно сгенерировать уникальную ссылку!')
