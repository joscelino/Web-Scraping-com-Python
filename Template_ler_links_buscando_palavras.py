# -*- coding: utf-8 -*-
"""
Web Scraping
Template de algortimo que le um link buscando palavras.
"""
# Importacao das bibliotecas
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Declaracao de variaveis
paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def getLinks(url_da_pagina):
    global paginas
    try:
        if url_da_pagina not in paginas_invalidas:
            html = urlopen(url_da_pagina)
            sopa = BeautifulSoup(html, "html.parser")
            lista_times = ('.paulo.|.gremio.|.palmeiras.|.santos.|.corinthians.')
            
            for link in sopa.find_all("a", href=re.compile(lista_times)):
                if "href" in link.attrs:
                    if link.attrs['href'] not in paginas and link.attrs['href'] not in paginas_invalidas:
                        nova_pagina = link.attrs['href']
                        print(nova_pagina)
                        paginas.add(nova_pagina)
                        getLinks(nova_pagina)
    except:
        paginas_invalidas.add(nova_pagina)
        
getLinks('https://globoesporte.globo.com/')
