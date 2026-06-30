from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 899.90},
    {"id": 2, "nome": "Mouse Gamer", "preco": 479.50}
]

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify(novo_produto), 201

if __name__ == "__main__":
    app.run(debug=True)
