import os #importa a biblioteca necessária para manipulação do S.O.
#####Comando abaixo só é necessário executar uma única vez
os.system("pip install mysql-connector-python") #Faz a instalação do conector MySQL

import mysql.connector #Importa o conector para o python se comunicar com o BD
import datetime #Importa a biblioteca datetime (data/hora)

def conectarBD(host, usuario, senha, DB):
    connection = mysql.connector.connect( #Informando os dados para conexão com o BD
        host = host, #ip do servidor do BD
        user= usuario, #Usuário do MySQL 
        password=senha, #Senha do usuário do MySQL
        database=DB  #nome do DB criado
    ) #Define o banco de dados usado
    return connection

#INSERT
def insert_BD(nome, rg, cpf, endereco, cidade, uf,conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "INSERT INTO CLIENTE(nome,rg,cpf,endereço,cidade,uf) VALUES (%s, %s, %s, %s,%s,%s)"
    data = (
    nome,
    rg,
    cpf,
    endereco,
    cidade,
    uf
    )

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    clientid = cursor.lastrowid #Obtém o último ID cadastrado

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o BD

    print("Foi cadastrado o novo cliente de ID:", clientid)

###READ
def read_BD(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM cliente" #Realizando um select para mostrar todas as linhas e colunas da tabela

    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtém todas as linhas no conjunto de resultados da consulta

    cursor.close() #fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Ler os registros existentes com o select
        print(result) #imprime os registros existentes

#UPDATE

def update_BD(id,nome, rg, cpf, endereco, cidade, uf,conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "UPDATE cliente SET nome = %s,rg = %s, cpf = %s, endereço = %s, cidade= %s,uf = %s WHERE id = %s"
    data = (nome,
            rg,
            cpf,
            endereco,
            cidade,
            uf,
            id
            )

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit()  #Efetua as modificações #altera os dados selecionados

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    print(recordsaffected, " registros alterados")

#DELETE
def delete_BD(id,conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "DELETE FROM cliente WHERE id = %s"
    data = (id,)

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    print(recordsaffected, " registros excluídos")

import time
while(True):
    os.system("clear")
    print("::::: GERENCIADOR DE CADASTRO DE CLIENTES :::::")
    print("1 - CADASTRAR NOVO CLIENTE")
    print("2 - LISTAR OS CLIENTES CADASTRADOS")
    print("3 - ATUALIZAR CADASTRO DO CLIENTE")
    print("4 - REMOVER CLIENTE CADASTRADO")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 0:
        break
    elif opcao == 1:
        nome = input("Digite o nome completo do cliente:")
        rg = input("Digite o RG:")
        cpf = input("Digite o CPF:")
        end = input("Digite o endereço:")
        cidade = input("Digite a cidade:")
        uf = input("Digite a sigla do estado (UF):")
        connection = conectarBD("localhost", "root", "admin", "projeto")
        insert_BD(nome,rg,cpf,end,cidade,uf, connection)
        time.sleep(3)
    elif opcao == 2:
        connection = conectarBD("localhost", "root", "admin", "projeto")
        print("Os registros existentes na tabela são:")
        read_BD(connection)
        time.sleep(3)
    elif opcao == 3: 
        id = input("Digite o id do cliente no qual deseja atualizar:")
        nome = input("Digite o novo nome do cliente:")
        rg = input("Digite o novo rg do cliente:")
        cpf = input("Digite o novo cpf do cliente:")
        endereço = input("Digite o novo endereço do cliente:")
        cidade = input("Digite a nova cidade do cliente:")
        uf = input("Digite o novo estado do cliente:")
        connection = conectarBD("localhost", "root", "admin", "projeto")
        update_BD(id,nome, rg, cpf, endereço, cidade, uf,connection)
        time.sleep(3)
    elif opcao == 4: 
        id = input("Digite o id do usuário no qual deseja deletar:")
        connection = conectarBD("localhost", "root", "admin", "projeto")
        delete_BD(id,connection)
        time.sleep(3)
    else:
        print("Opção inválida!")
        time.sleep(3)