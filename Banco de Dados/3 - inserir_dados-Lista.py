import sqlite3 as s
lista=[(4,"Tonner",40,"SP"),(5, "Tablet",10,"PR")]

conex=s.connect("estoque.db")

cursor= conex.cursor()

cursor.executemany('''INSERT INTO tabProd(tbCod,tbNome,tbQtde,tbEstado) VALUES(?,?,?,?)''', lista)

conex.commit()
cursor.close()
conex.close()