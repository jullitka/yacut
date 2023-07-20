from re import match

from flask import jsonify, request

from . import app, db
from .constants import REGEX_PATTERN
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_url


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    elif 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    elif 'custom_id' not in data or data['custom_id'] in (None, ''):
        data['custom_id'] = get_unique_short_url()
    elif URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f'''Имя "{data['custom_id']}" уже занято.''')
    elif not match(REGEX_PATTERN, data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url_map = URLMap(original=data['url'],
                     short=data['custom_id'])
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original})
