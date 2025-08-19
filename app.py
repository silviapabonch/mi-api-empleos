from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista en memoria de vacantes
vacantes = []

@app.route("/vacantes", methods=["GET"])
def listar_vacantes():
    return jsonify(vacantes)

@app.route("/vacantes", methods=["POST"])
def crear_vacante():
    data = request.json
    vacantes.append(data)
    return jsonify({"mensaje": "Vacante creada con éxito", "vacante": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
