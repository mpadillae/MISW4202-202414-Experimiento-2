from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import requests
import json



# -----------------------------------------------------------
# ------------------------ Configuración Inicial ------------
# -----------------------------------------------------------

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///pqrs.db" )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.before_request
def create_tables():
    db.create_all()


# -----------------------------------------------------------
# ------------------------ Modelos --------------------------
# -----------------------------------------------------------


class PQR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(85), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    solicitante = db.Column(db.String(30),  nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    activo = db.Column(db.Boolean, nullable=False)
    severidad = db.Column(db.Integer, nullable=False)
   
class PQRSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = PQR
        load_instance = True

pqr_schema = PQRSchema()

# -----------------------------------------------------------
# ------------------------ Endpoint  --------------------------
# -----------------------------------------------------------

# Endpoint para consulta de los PQRs
@app.route("/pqr", methods=["GET"])
def consulta_pqr():
    
    token = request.json["token"]
    response = requests.post(
        "http://127.0.0.1:8092/verificar_token",
        json=json.dumps({"token": token}),
        headers={"Content-Type": "application/json"},
    )
    if response.status_code == 401 or response.status_code == 403:
        return jsonify({"error": "Acceso no autorizado a la informacion de PQRs"}), 401
    else:
        return [pqr_schema.dump(pqr) for pqr in PQR.query.all()], 200


if __name__ == "__main__":
    app.run(debug=True, port=8091)