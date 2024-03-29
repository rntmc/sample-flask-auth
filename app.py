from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Caminho onde o bd sera conectado

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
#view login
login_manager.login_view = 'login'
# Session <- conexao ativa

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password") # Recebemos credenciais no corpo da requisicao

  if username and password: # conferir se tem username e password
    #Login
    user = User.query.filter_by(username=username).first() #query eh um metodo do SQLAlchemy que permite buscar dados no bd. Utilizamos first pq retornara uma lista e pegamos o primeiro
    
    if user and user.password == password: # verifamos se encontramos usauario e se a senha cadastrada bate com o que recebemos
      login_user(user) # fazemos autenticacao do usuario. Fica salvo nos cookies
      print(current_user.is_authenticated) # printa se o usuario ta autenticado ou nao
      return jsonify({"message": "Autenticacao realizada com sucesso"})

  return jsonify({"message": "Credenciais invalidas"}), 400

@app.route("/logout", methods=["GET"])
@login_required #rota protegida. Usuario nao podera solicitar essa rota sem estar autenticado
def logout():
  logout_user()
  return jsonify({"message": "Logout realizado com sucesso!"})


@app.route("/", methods=["GET"])
def hello_world():
  return "Hello World"

if __name__ == "__main__":
  app.run(debug=True)