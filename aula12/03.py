
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("tarefas.db")
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route("/tarefas", methods=["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM tarefas")
    tarefas = [dict(t) for t in cursor.fetchall()]
    conexao.close()
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar():
    dados = request.get_json()

    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO tarefas (titulo, feita) VALUES (?, ?)",
        (dados["titulo"], dados.get("feita", 0))
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return jsonify({"id": novo_id, **dados}), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE tarefas SET titulo = ?, feita = ? WHERE id = ?",
        (dados["titulo"], dados["feita"], id)
    )
    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    conexao.close()
    return jsonify({"id": id, **dados})

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar(id):
    conexao = conectar()

    cursor = conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    conexao.close()
    return jsonify({"mensagem": "Tarefa apagada com sucesso"})

if __name__ == "__main__":
  app.run(debug=True)


POST http://127.0.0.1:5000/tarefas
Content-Type: application/json

{
    "titulo": "Estudar API REST",
    "feita": 0
}


GET http://127.0.0.1:5000/tarefas


PUT http://127.0.0.1:5000/tarefas/1
Content-Type: application/json

{
    "titulo": "Estudar CRUD completo",
    "feita": 1
}


DELETE http://127.0.0.1:5000/tarefas/1
