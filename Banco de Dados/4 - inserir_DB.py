import sqlite3 as s

db = "estoque.db"#variavel para guardar o nome do banco
conex= s.connect(db)
cursor = conex.cursor()

resposta = "s" #variavel de controle do while
while(resposta.upper() =='S'):    
    try:
       
        w_cod = int(input("Código do Protocolo: "))
        w_nome = input("Nome do produto: ")
        w_qtde = int(input("Quantidade: "))
        w_estado = input("Estado: ")

        inserir = "s"
        cursor.execute('''INSERT INTO tabProd(tbCod,tbNome,tbQtde,tbEstado) VALUES(?,?,?,?)''',(w_cod, w_nome,w_qtde,w_estado))
    except s.IntegrityError:
        print("=========================")
        print("=== Chave inexistente ===", w_cod)
        print("=========================")

    resposta = input("Deseja continuar? (s/n)")

    if(inserir == 's'):
        conex.commit()
    cursor.close()
    conex.close()


