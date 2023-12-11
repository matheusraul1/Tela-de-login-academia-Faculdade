from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
import sys
import os #importa a biblioteca necessaria para manipulação do S.O.
os.system("pip install mysql-connector-python") #Faz a instalção do mysql
import mysql.connector #importa o conector para o python se comunicar
####Comando abaixo só é necessário executar uma única vez

def conectarBD(host, usuario, senha, DB):
    connection = mysql.connector.connect( #Informando os dados para conexão com o BD
        host = host, #ip do servidor do BD
        user= usuario, #Usuário do MySQL 
        password=senha, #Senha do usuário do MySQL
        database=DB  #nome do DB criado
    ) #Define o banco de dados usado

    return connection

#INSERT
def insert_BD(nome, rg, cpf, endereco, cidade, uf):
    connection = conectarBD("localhost", "root", "admin", "projeto") #Recebe a conexão estabelecida com o banco
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

def inserir():
    nome = telaCadastro.txtnome.text()
    rg = telaCadastro.txtRG.text()
    cpf = telaCadastro.txtCPF.text()
    end = telaCadastro.txtendereco.text()
    cidade = telaCadastro.txtCidade.text()
    uf = telaCadastro.txtUF.text()
    insert_BD(nome, rg, cpf, end, cidade, uf)
def limpar():
    telaCadastro.txtnome.setText("")
    telaCadastro.txtRG.setText("")
    telaCadastro.txtCPF.setText("")
    telaCadastro.txtendereco.setText("")
    telaCadastro.txtCidade.setText("")
    telaCadastro.txtUF.setText("")

app = QtWidgets.QApplication(sys.argv)
telaCadastro = uic.loadUi('cadastro.ui')
telaCadastro.show()
telaCadastro.btnCadastrar.clicked.connect(inserir)
telaCadastro.btnLimpar.clicked.connect(limpar)
#telaMenu.btnTelaCadastro.clicked.connect(AbrirTelaCadastro)
app.exec()