import sqlite3

conex=sqlite3.connect("estoque.db") #CRIAR CONEXÃO COM O BANCO

cursor = conex.cursor()# ENVIAR COMANDOS PARA O BANCO

#EXECUTAR UM CONJUNTO DE COMANDO
cursor.execute('''
        CREATE TABLE tabProd(tbCod INTERGER PRIMARY KEY,
        tbNome TEXT,
        tbQtde INTERGER,
        tbEstado TEXT)
''')

cursor.close()#fecha o cursor
conex.close()#fecha conexão com banco