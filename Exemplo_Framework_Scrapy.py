# -*- coding: utf-8 -*-
"""
Web scraping utilizando a biblioteca Scrapy
"""
# Importacao das bibliotecas
import scrapy

# Definindo a classe
class SpiderCitacoes(scrapy.Spider):
    name = 'citacoes' # Esse nome deve ser exclusivo dentro de um projeto. Diferentes spiders, diferentes nomes
    
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
            'http://quotes.toscrape.com/page/2/'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, resposta):
        pagina = resposta.url.split("/")[-2]
        nome_arquivo = f'citacoes-{pagina}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(resposta.body)
        self.log(f'Arquivo salvo {nome_arquivo}')
