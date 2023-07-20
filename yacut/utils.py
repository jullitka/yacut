from random import choice

from .constants import ALLOWED_SYMBOLS, LEN_SHORT_STRING
from .models import URLMap


def get_unique_short_url():
    """Генерирует случайную ссылку"""
    while True:
        short = ''
        for _ in range(LEN_SHORT_STRING):
            short += choice(ALLOWED_SYMBOLS)
        if not URLMap.query.filter_by(short=short).first():
            return short
