from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pedido

bp_pedido = Blueprint('pedido', __name__, template_folder="templates")

@bp_pedido.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedido.html', dados=dados)

@bp_pedido.route('/add')
def add():
    return render_template('pedido_add.html')

@bp_pedido.route('/save', methods=['POST'])
def save():
    usuario_id = request.form.get('usuario_id')
    pizza_id = request.form.get('pizza_id')
    data = request.form.get('data')
    if usuario_id and pizza_id and data:
        objeto = Pedido(usuario_id, pizza_id, data)
        db.session.add(objeto)
        db.session.commit()
        flash("Pedido salvo com sucesso!")
        return redirect('/pedidos')
    else:
        flash("Preencha todos os campos")
        return redirect('/pedidos/add')