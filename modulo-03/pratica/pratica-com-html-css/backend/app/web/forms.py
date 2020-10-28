from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class GeneroForm(FlaskForm):
    nome = StringField('Digite o seu nome',
                       id='nome',
                       validators=[InputRequired('Nome é requerido')])
    submeter = SubmitField('Enviar')
