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


#insere os valores no banco de dados
cursor.execute(
    """ 
INSERT INTO ESTOQUE(NOME, PRECO, QUANTIDADE) 
VALUES ('Arroz', 5.7, 10)
"""
)

cursor.execute(
    """ 
INSERT INTO ESTOQUE(NOME, PRECO, QUANTIDADE) 
VALUES ('Feijão', 9.5, 7)
"""
)
#commit e fecha a conexão
conexao.commit()
conexao.close()
