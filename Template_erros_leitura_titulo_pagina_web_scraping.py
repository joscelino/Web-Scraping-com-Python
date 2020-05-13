# -*- coding: utf-8 -*-
"""
Template para tratar erros de leitura de titulos de paginas web 
durante a realizacao de um web scraping
"""
# Importacao das bibliotecas
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# Funcao para tratar erros de retorno na leitura dos titulos das paginas web
def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print("Ocorreu erro HTTP: {erro}")
        return None
    except URLError as erro:
        print("Ocorreu erro URL: {erro}")
        return None
    except:
        print("Ocorreu erro na pagina!")
        return None
    
    try:
        sopa = BeautifulSoup(html.read(), "html.parser")
        titulo = sopa.body.h1
    except  AttributeError as erro:
        print("Ocorreu erro ao acessar a tag: {erro}")
        return None
    except:
        print("Ocorreu erro ao acessar o conteudo da pagina!")
        return None
    
    return titulo

titulo = getTitulo(input("Informe a URL completa: "))

if titulo is not None:
    print(titulo)
else:
    print("Titulo nao encontrado!")
        
