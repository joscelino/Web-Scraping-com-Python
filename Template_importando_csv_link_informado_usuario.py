# -*- coding: utf-8 -*-
"""
Importando aquivo csv atraves de link informado por usuario
"""
# Importacao das bibliotecas
from urllib.request import urlretrieve
import csv

link = input("Informe o numero do arquivo csv: ")
delimitador = input("Informe o deliminitador (',' ou ';') : ")
urlretrieve(link, "arquivo_baixado.csv")

# Impressao das linhas do arquivo
with open("arquivo_baixado.csv", 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter=delimitador)
    for linha in reader:
        print(linha)
