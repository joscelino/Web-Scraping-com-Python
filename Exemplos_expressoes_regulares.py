# -*- coding: utf-8 -*-
"""
Expressoes Regulares
"""
# Importar bibliotecas
import re
from pprint import pprint

# Funcoes da biblioteca 
# findall   - encontra todas as expressoes do padrao procurado dentro do texto
# search    - econtra a primeira ocorrencia do padrao procurado
# sub       - substituir algo dentro do texto
# compile   - compilar expressao regular para reutilizar

# Criar string para teste
string = 'Este eh um teste de expressoes regulares'

# Buscando um padrao
print(re.search(r'teste', string))
print(re.findall(r'teste', string))

# Substituindo a expressao
print(re.sub(r'eh', 'EH', string))

# Compilando a expressao regular
ex_regular = re.compile(r'teste')

# Buscando apos compilar a expressao regular
ex_regular.search(string)
ex_regular.findall(string)
ex_regular.sub('TESTE', string)

# Meta caracteres
''' .  ^ $ | [ ] ( ) \. 
| - significa OU
. - significa qualquer caractere (com excessao da quebra de linha)
[] - conjunto de caracteres

'''

piada = '''Durante o jantar, Joãozinho conversa com a mãe: 
- Mamãe, porque é que o papai é careca? 
- Ora, filhinho.... Porque ele tem muitas coisas para pensar e é muito inteligente! 
- Mas mamãe....então porque é que você tem tanto cabelo? 
- Cala a boca e come logo esta po*ra de sopa, menino!'''

print(re.findall(r'Joãozinho|Mamãe|papai',piada))
print(re.findall(r'.oãozinho|.amãe|.apai|...que',piada))
print(re.findall(r'[Mm]amãe',piada))
print(re.findall(r'[a-zA-Z]amãe',piada))
print(re.findall(r'JOãoziNho|MaMãe|papai',piada, flags=re.IGNORECASE))

# Quantificadores
'''
?   - 0 ou 1 vez
*   - 0 ou n vezes 
+   - 1 ou n vezes
{ } - n especifico  ou {min, max}

'''
print(re.findall(r'JOão*ziNhO+',piada, flags=re.IGNORECASE))
print(re.sub(r'JOão*ziNhO+', 'Felipe',piada, flags=re.IGNORECASE))

texto = 'Joao ama ser amado!'
print(re.findall(r'ama[do]{2}',texto, flags=re.IGNORECASE))
print(re.findall(r'ama[do]{0,2}',texto, flags=re.IGNORECASE))
print(re.findall(r'ama[do]*',texto, flags=re.IGNORECASE))

# Greedy e non-greedy (lazy)
# Texto ambiguo
texto_g = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>',texto_g))
print(re.findall(r'<[pdiv]{1,3}>.*',texto_g))
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto_g)) # Comportamento guloso (greedy)
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto_g)) # Comportamento nao-guloso (non greedy)
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>',texto_g)) # Comportamento nao-guloso (non greedy)

# Grupos e retrovisores
'''
( ) - 
'''
print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>',texto_g))
tags = re.findall(r'(<([pdiv]{1,3})>.+?<\/\2>)',texto_g)

for tag in tags:
    um, dois = tag
    print(tag)
    print(tag[0])
    print(tag[1])
    print(um)

cpf = '154.325.601-99'

print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', cpf))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})', cpf))

'''
^ - comeca com
$ - termina com
[^a-d] - negacao
'''
print(re.findall(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', cpf))

cpf2 = 'a 154.325.601-99'
print(re.findall(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', cpf2))

# Valor exatamente no mesmo formato
print(re.findall(r'^([0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})$', cpf))

# Traz valor com negacao 
print(re.findall(r'^([^6-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))

# shothands e flags importantes
print(re.findall(r'[a-z]',piada))
print(re.findall(r'[a-z]+',piada))
print(re.findall(r'[a-z]+',piada, flags=re.I))
print(re.findall(r'[a-zAZ0=9]+',piada))
print(re.findall(r'\w+',piada))
print(re.findall(r'\w+',piada, flags=re.A))
print(re.findall(r'\W+',piada))
print(re.findall(r'\W+',piada, flags=re.A))
print(re.findall(r'\d+',piada))
print(re.findall(r'\D+',piada))
print(re.findall(r'\s+',piada, flags=re.I))
print(re.findall(r'\S+',piada, flags=re.I))
print(re.findall(r'\bfil\w+',piada, flags=re.I))
print(re.findall(r'\w+ente\b',piada, flags=re.I))
print(re.findall(r'\b\w{4}\b',piada, flags=re.I))
print(re.findall(r'\w{4}',piada, flags=re.I))

cpfs = '''
115.742.854-65
042.325.858-21
199.851.526-75
'''
print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}',cpfs))

cpfs2 = '''
115.742.854-65      ABC
042.325.858-21      DEF
199.851.526-75
'''
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$',cpfs2, flags=re.M))

# Lookahead e Lookbehind

ips = '''
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
'''

print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',ips))
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)',ips))

# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)',ips))

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)',ips))

pprint(re.findall(r'(?=.*inactive).+', ips))
pprint(re.findall(r'(?=.*active).+', ips))
pprint(re.findall(r'(?=.*[^n]active).+', ips))

# Positive lookbehind
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',ips))

# Negative lookbehind
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',ips))
