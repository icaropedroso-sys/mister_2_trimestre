import sqlite3

conexao = sqlite3.connect("biblioteca.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
)
""")

conexao.execute("INSERT INTO autores (nome) VALUES (?)", ("Adolf Hitler",))
conexao.execute("INSERT INTO autores (nome) VALUES (?)", ("George Orwell",))

conexao.execute(
    "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
    ("My Kampf", 1)
)

conexao.execute(
    "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
    ("1984", 2)
)

conexao.execute(
    "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
    ("A Revolução dos Bichos", 2)
)
