from flask import abort, flash, redirect, render_template

from . import app
from .forms import ShortURLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def add_short_url():
    form = ShortURLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = URLMap.get_unique_random_short_id()
        elif URLMap.is_short_id(short):
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        url = URLMap(
            original=form.original_link.data,
            short=short,
        )
        url.add_to_db()
        return render_template('index.html', form=form, short=short), 200
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirection(short):
    url_map = URLMap.is_short_id(short)
    if url_map:
        return redirect(url_map.original)
    abort(404)