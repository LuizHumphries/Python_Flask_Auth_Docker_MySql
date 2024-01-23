from flask import Flask, jsonify, request
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    """Load user from db"""
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    """Login"""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        #username
        user = User.query.filter_by(username=username).first()
        if user and user.password == password: 
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação concluida com sucesso"})
    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    """Logout"""
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

@app.route('/user', methods=['POST'])
def create_user():
    """Create user"""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = User(username=username, password= password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário cadastrado com sucesso"})
    return jsonify({"message": "Credenciais inválidas"}), 400



if __name__ == "__main__":
    app.run(debug=True)