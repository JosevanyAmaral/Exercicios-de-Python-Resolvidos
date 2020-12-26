from urllib import request, error
try:
    site = request.urlopen("http://www.pudim.com.br")
except error.URLError:
    print('\033[1;31mO site Pudim não está acessível no momento.')
else:
    print('\033[1;32mConsegui acessar o site Pudim com sucesso.\033[m')
    print(site.read)