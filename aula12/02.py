from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("produtos.db")
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route("/produtos", methods=["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM produtos")
    produtos = [dict(p) for p in cursor.fetchall()]
    conexao.close()
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar():
    dados = request.get_json()

    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (dados["nome"], dados["preco"])
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return jsonify({"id": novo_id, **dados}), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE produtos SET nome = ?, preco = ? WHERE id = ?",
        (dados["nome"], dados["preco"], id)
    )
    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()
        return jsonify({"erro": "Produto não encontrado"}), 404

    conexao.close()
    return jsonify({"id": id, **dados})

@app.route("/produtos/<int:id>", methods=["DELETE"])
def apagar(id):
    conexao = conectar()

    cursor = conexao.execute(
        "DELETE FROM produtos WHERE id = ?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()
        return jsonify({"erro": "Produto não encontrado"}), 404

    conexao.close()
    return jsonify({"mensagem": "Produto apagado com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)
