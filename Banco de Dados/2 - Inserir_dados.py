import sqlite3 as s

conex =s.connect("estoque.db")

cursor=conex.cursor()

cursor.execute('''INSERT INTO tabProd(tbCod,tbNome,tbQtde,tbEstado) VALUES(2, "teclado", 15, "SP")
''')
cursor.execute('''INSERT INTO tabProd(tbCod,tbNome,tbQtde,tbEstado) VALUES(3, "mouse", 20, "RJ")
''')

conex.commit()#transferindo a informação da memoria para o banco
cursor.close()
conex.close()
