# -*- coding: utf-8 -*-
"""
Armazenando dados em arquivo csv
"""
# Importacao das bibliotecas
import csv

# Escrevendo arquivos csv

arquivo = open("exemplo.csv", "w", newline = "")
try:
    writer = csv.writer(arquivo)
    writer.writerow(['Nome', 'Telefone', 'Cidade'])
    writer.writerow(['AAAAA', '9999999', 'nononono'])
    writer.writerow(['BBBBB', '8888888', 'onononon'])
    writer.writerow(['CCCCC', '7777777', 'abababab'])
        
finally:
    arquivo.close()

# Lendo arquivos csv
with open('nome_arquivo.csv') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter=',')
    for linha in reader:
        print(linha)

