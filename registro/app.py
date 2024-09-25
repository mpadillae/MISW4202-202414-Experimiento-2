from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import bcrypt

# -----------------------------------------------------------
# ---------------------- Configuración ----------------------
# -----------------------------------------------------------

# Usando SQLite como almacenamiento para el registro de usuarios.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///usuarios.db")
db = SQLAlchemy(app)

@app.before_request
def create_tables():
    db.create_all()

# -----------------------------------------------------------
# ------------------------- Modelos -------------------------
# -----------------------------------------------------------

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# -----------------------------------------------------------
# ------------------------ Endpoints ------------------------
# -----------------------------------------------------------

# Endpoint para que un usuario se registre.
@app.route("/user/signup", methods=["POST"])
def registrar_usuario():
    if "username" not in request.json or "password" not in request.json:
        return jsonify({"error": "Ingresa un nombre de usuario y una contraseña."}), 400

    usuario = Usuario(username=request.json["username"], 
                      password=request.json["password"])

    try:
        db.session.add(usuario)
        db.session.commit()
        return jsonify({"message": "Usuario registrado correctamente."}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Nombre de usuario ya existe."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Endpoint obtener los datos encriptados del usuario.
@app.route("/user/encrypt", methods=["GET"])
def encriptar_usuario():
    username = request.args.get("username")

    if not username:
        return jsonify({"error": "Ingrese un nombre de usuario."}), 400

    usuario = Usuario.query.filter_by(username=username).first()

    if usuario:
        hash_password = bcrypt.hashpw(usuario.password.encode(), salt=bcrypt.gensalt())
        return jsonify({"hash": bytes.decode(hash_password)}), 200
    else:
        return jsonify({"error": "No se encontró el usuario en la base de datos."}), 404


if __name__ == "__main__":
    app.run(debug=True, port=8090)
