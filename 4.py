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

cursor.execute(
    """ 
INSERT INTO CLIENTE(NOME, SOBRENOME, IDADE, PESO, SEXO, RENDA) 
VALUES ('Yun', 'Z', 27, 70.7, 'M',1500)
"""
)

cursor.execute(
    """ 
INSERT INTO CLIENTE(NOME, SOBRENOME, IDADE, PESO, SEXO, RENDA) 
VALUES ('Ching', 'A', 30, 92.3, 'M', 2500)
"""
)

cursor.execute(
    """ 
INSERT INTO CLIENTE(NOME, SOBRENOME, IDADE, PESO, SEXO, RENDA) 
VALUES ('Angelina', 'A', 19, 57.9, 'F', 1700)
"""
)

#commit e fecha a conexão
conexao.commit()
conexao.close()
