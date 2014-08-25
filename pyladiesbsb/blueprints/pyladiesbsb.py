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
    noticias = get_table('noticias')
    todas_as_noticias = noticias.all()
    return render_template('index.html',
                           noticias=todas_as_noticias,
                           title=u"Todas as notícias")

@pyladiesbsb_blueprint.route("/log")
@pyladiesbsb_blueprint.route("/log/<int:log_id>")
def log(log_id=0):
    if log_id:
        logs = get_table('noticias')
        log = logs.find_one(id=log_id)
        return render_template('log.html', log=log)
    else:
        return render_template('log.html')



@pyladiesbsb_blueprint.route("/log/cadastro", methods=["GET", "POST"])
def loggin():
    noticias = get_table('noticias')
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename

        id_nova_noticia = noticias.insert(dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                               id_nova_noticia=id_nova_noticia)

    return render_template('log.html', title=u"Inserir nova noticia")


@pyladiesbsb_blueprint.route("/eventos/")
def eventos():
    return render_template('eventos.html')


@pyladiesbsb_blueprint.route("/contato/")
def contato():
    return render_template('contato.html')

@pyladiesbsb_blueprint.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)
