from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Usuario

bp_usuario = Blueprint('usuario', __name__, template_folder="templates")

@bp_usuario.route('/')
def index():
    dados = Usuario.query.all()
    return render_template('usuario.html', dados=dados)

@bp_usuario.route('/add')
def add():
    return render_template('usuario_add.html')

@bp_usuario.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    if nome and email and senha:
        objeto = Usuario(nome, email, senha)
        db.session.add(objeto)
        db.session.commit()
        flash("Usuario salvo com sucesso!")
        return redirect('/usuarios')
    else:
        flash("Preencha todos os campos")
        return redirect('/usuarios/add')