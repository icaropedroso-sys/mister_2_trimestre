import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

produtos = [
    ("Mouse Gamer", 349.99),
    ("Teclado Mecânico", 899.90),
    ("Monitor 24'", 1499.00)
]

cursor.executemany("INSERT INTO produtos (nome, preco) VALUES (?, ?)", produtos)

conexao.commit()
conexao.close()
