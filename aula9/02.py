from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Mouse Gamer", "preco": 349.99, "disponivel": True},
    {"id": 2, "nome": "Monitor 24'", "preco": 1499.00, "disponivel": False},
    {"id": 3, "nome": "Headset USB", "preco": 529.50, "disponivel": True},
    {"id": 4, "nome": "Webcam HD", "preco": 410.00, "disponivel": True}
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)
