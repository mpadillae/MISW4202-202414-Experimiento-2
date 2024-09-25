from flask import Flask, jsonify, request
import random
import jwt
from datetime import datetime, timedelta
import requests
import bcrypt
import json

app = Flask(__name__)

# -----------------------------------------------------------
# ---------------------- Configuración ----------------------
# -----------------------------------------------------------
contrasena_correcta = 'password123'
hash_contrasena_correcta = bcrypt.hashpw(contrasena_correcta.encode('utf-8'), bcrypt.gensalt())

otp_generado = None
token_secreto = "Apdasda56978"


# Función para generar un OTP de 4 dígitos
def generar_otp():
    return str(random.randint(1000, 9999))


# Función para generar un token JWT
def generar_token():
    fecha_acceso = datetime.utcnow()
    payload = {"fecha_acceso": fecha_acceso.isoformat()}
    token = jwt.encode(payload, token_secreto, algorithm="HS256")
    return token

# -----------------------------------------------------------
# ---------------------- Endpoints ------------------------
# -----------------------------------------------------------

# Endpoint para el inicio de sesión
@app.route("/user/login", methods=["POST"])
def iniciar_sesion():
    global otp_generado

    info = request.get_json()
    provided_password = info.get("password")
    # Llamada al endpoint de registro para obtener el hash de la contraseña registrada
    respuesta = requests.get(
        "http://127.0.0.1:8090/user/encrypt",
        params={"username": info.get("username")},
    )  # Reemplazar con la URL real del servicio de registro
    hash_contrasena_correcta = respuesta.json().get("hash")

    if not provided_password or not bcrypt.checkpw(
        password=str.encode(provided_password),
        hashed_password=str.encode(hash_contrasena_correcta),
    ):
        return jsonify({"error": "Contraseña incorrecta"}), 401
    else:
        otp_generado = generar_otp()
        return (jsonify({"mensaje": "OTP generado con éxito", "otp": otp_generado}),200,)


# Endpoint para verificar el OTP
@app.route("/verificar_otp", methods=["POST"])
def verificar_otp():
    global otp_generado

    datos = request.get_json()
    otp_proporcionado = datos.get("otp")

    if otp_generado is not None:
        if otp_proporcionado == otp_generado:
            token = generar_token()
            otp_generado = None
            return jsonify({"verificado": True, "token": token}), 200
        else:
            return jsonify({"verificado": False}), 401
    else:
        return jsonify({"error": "OTP no generado aún"}), 400


# Endpoint para verificar el token
@app.route("/verificar_token", methods=["POST"])
def verificar_token():
    datos = request.get_json()
    token_proporcionado = json.loads(datos).get("token")

    try:
        decoded_payload = jwt.decode(token_proporcionado, token_secreto, algorithms=["HS256"])
        return jsonify({"verificado": True, "decoded_payload": decoded_payload}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "El token ha expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401


if __name__ == "__main__":
    app.run(debug=True, port=8092)