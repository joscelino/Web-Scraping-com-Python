# -*- coding: utf-8 -*-
"""
Armazenando dados obtidos por web scraping
"""
# Importacao das bibliotecas
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
import os

# Definicao das varivais
downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

# Funcao que faz tratamento na url informada para retornar apenas links do proprio site
def getAbsoluteURL(baseUrl , source):
    if source.startswith ("http://www."):
        url = "http://"+source[11:]
    elif source.startwith("http://"):
        url = "http://"+source
    else:
        url = url+"/"+source
    if baseUrl not in url or ".js" in url:
        return None
    return url

# Criar pastas localmente segundo o caminho dos arquivos que serao baixados
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path
    directory = os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    return path

html = urlopen("http://pythonscraping.com")
sopa = BeautifulSoup(html, "html.parser")
downloadList = sopa.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))