# -*- coding: utf-8 -*-
"""
Template de conexao Python com MySQL
"""
# Importacao da biblioteca
import pymysql

##############################################################################
#
# CONEXAO USANDO PARAMETROS DECLARADOS EM VARIAVEIS
#
##############################################################################

# Parametros de conexao
host = 'localhost'
id_user = ''
password = ''
data_base = 'produtos'

# Comando a ser realizado no MySQL
sql = 'select * from produtos'

# integracao com Banco de dados MySql
conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)
cursor = conexao.cursor()
cursor.execute(sql)

# Fechando a conexao
cursor.close()
conexao.close()

##############################################################################
#
# CONEXAO USANDO DICIONARIO
#
##############################################################################

# Criando dicionario com dados de conexao
configuracao = {
    'host' :'localhost',
    'user' : '',
    'passwd' : '',
    'db' : 'produtos'
    }

# Comando a ser realizado no MySQL
sql = 'select * from produtos'

# integracao com Banco de dados MySql
conexao = pymysql.connect(**configuracao)
cursor = conexao.cursor()
cursor.execute(sql)


# Fechando a conexao
cursor.close()
conexao.close()
