from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = "QualquerCoisaSecreta"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Usuario, Pizza, Pedido

from modulos.usuarios.usuarios import bp_usuario
app.register_blueprint(bp_usuario, url_prefix='/usuarios')

from modulos.pizzas.pizzas import bp_pizza
app.register_blueprint(bp_pizza, url_prefix='/pizzas')

from modulos.pedidos.pedidos import bp_pedido
app.register_blueprint(bp_pedido, url_prefix='/pedidos')


@app.route('/')
def index():
    return render_template('ola.html')