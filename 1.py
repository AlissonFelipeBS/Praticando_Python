import sqlite3

#cria a conexão
conexao = sqlite3.connect('estoque.db')
#cria o objeto cursor
cursor = conexao.cursor()
#deleta a tabela CLIENTE caso já exista
cursor.execute('DROP TABLE IF EXISTS ESTOQUE')
#cria a tabela
sql = """CREATE TABLE ESTOQUE(
    NOME TEXT,
    PRECO FLOAT,
    QUANTIDADE INT
    )"""
cursor.execute(sql)
#commit e fecha a conexão
conexao.commit()
conexao.close()
