import sqlite3

#cria a conexão
conexao = sqlite3.connect('cliente.db')
#cria o objeto cursor
cursor = conexao.cursor()
#deleta a tabela CLIENTE caso já exista
cursor.execute('DROP TABLE IF EXISTS CLIENTE')
#cria a tabela
sql = """CREATE TABLE CLIENTE(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME CHAR(30) NOT NULL,
    SOBRENOME CHAR(20),
    IDADE INT,
    PESO FLOAT,
    SEXO CHAR(1),
    RENDA FLOAT
    )"""
cursor.execute(sql)
#commit e fecha a conexão
conexao.commit()
conexao.close()
