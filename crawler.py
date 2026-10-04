import requests
from bs4 import BeautifulSoup


URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Erro ao fazer requisição")
    except Exception as error:
        print("Erro ao fazer requisição")
        print(error)


resposta = buscar(URL_AUTOMOVEIS) #tira a # para rodar
if resposta:
    soup = BeautifulSoup(resposta, 'html.parser')
    print(soup.prettify())