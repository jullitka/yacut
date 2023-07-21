from re import match

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .constants import REGEX_PATTERN


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    elif 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    elif 'custom_id' not in data or data['custom_id'] in (None, ''):
        data['custom_id'] = URLMap.get_unique_random_short_id()
    elif URLMap.is_short_id(data['custom_id']):
        raise InvalidAPIUsage(f'''Имя "{data['custom_id']}" уже занято.''')
    elif not match(REGEX_PATTERN, data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url_map = URLMap(original=data['url'],
                     short=data['custom_id'])
    url_map.add_to_db()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.is_short_id(short_id)
    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original})
