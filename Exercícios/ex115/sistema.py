from ex115.lib.interface import cadastro
from ex115.lib.arquivo import *
arq = 'arquivo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
opcao = cadastro(arq)
