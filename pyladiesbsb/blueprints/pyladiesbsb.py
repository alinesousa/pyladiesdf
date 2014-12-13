# coding: utf-8
import os

from werkzeug import secure_filename
from flask import (
    Blueprint, request, current_app, send_from_directory, render_template
)

from ..db import get_table

pyladiesbsb_blueprint = Blueprint('pyladiesbsb', __name__)


@pyladiesbsb_blueprint.route("/")
def index():
    logs = get_table('logs')
    todos_os_logs = logs.all()
    return render_template('index.html',
                           logs=todos_os_logs,
                           title=u"Todas as notícias")


@pyladiesbsb_blueprint.route("/log")
@pyladiesbsb_blueprint.route("/log/<int:log_id>")
def log(log_id=0):
    if log_id:
        logs = get_table('logs')
        log = logs.find_one(id=log_id)
        return render_template('log.html', log=log)
    else:
        logs = get_table('logs')
        todos_os_logs = logs.all()
        return render_template('log.html',
                               logs=todos_os_logs,
                               title=u"Todas as notícias")


@pyladiesbsb_blueprint.route("/logging", methods=["GET", "POST"])
def logging():
    logs = get_table('logs')
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename

        id_nova_noticia = logs.insert(dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                               id_nova_noticia=id_nova_noticia)

    return render_template('logging.html')


@pyladiesbsb_blueprint.route("/signin", methods=["GET", "POST"])
def signin():
    logs = get_table('logs')
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename

        id_nova_noticia = logs.insert(dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                               id_nova_noticia=id_nova_noticia)

    return render_template('signin.html')


@pyladiesbsb_blueprint.route("/eventos")
def eventos():
    return render_template('eventos.html')


@pyladiesbsb_blueprint.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)
