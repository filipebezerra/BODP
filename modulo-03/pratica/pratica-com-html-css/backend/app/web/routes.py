from flask import render_template, redirect
from flask.helpers import url_for
from . import web_blueprint as web
from .forms import GeneroForm


@web.route('/genero', methods=['GET', 'POST'])
def genero():
    form = GeneroForm()
    if form.validate_on_submit():
        return redirect(url_for('web.bemvindo'))
    return render_template('index.html', form=form, titulo='Gênero')


@web.route('/bemvindo')
def bemvindo():
    return render_template('bemvindo.html', titulo='Bem-vindo')