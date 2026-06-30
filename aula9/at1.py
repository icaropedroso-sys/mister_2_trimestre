from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def obter_produto():
    produto = {
        "id": 101,
        "nome": "Teclado Mecânico",
        "preco": 259.90,
        "disponivel": True
    }
    return jsonify(produto)

if __name__ == "__main__":
    app.run(debug=True)
