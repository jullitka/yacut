from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import ShortURLForm
from .models import URLMap
from .utils import get_unique_short_url


@app.route('/', methods=['GET', 'POST'])
def add_short_url():
    form = ShortURLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short or short == '':
            short = get_unique_short_url()
        elif URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        url = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        return render_template('index.html', form=form, short=short), 200
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirection(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map:
        return redirect(url_map.original)
    abort(404)