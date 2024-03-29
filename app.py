from flask import Flask
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Caminho onde o bd sera conectado

db.init_app(app)
# Session <- conexao ativa

@app.route("/", methods=["GET"])
def hello_world():
  return "Hello World"

if __name__ == "__main__":
  app.run(debug=True)