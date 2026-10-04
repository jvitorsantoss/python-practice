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


def parsear_anuncios(html):
    soup = BeautifulSoup(html, 'html.parser')
    anuncios = []
    for card in soup.find_all('a', class_='card'):
        anuncios.append({
            'titulo': card.find('div', class_='header').get_text(strip=True),
            'preco': card.find('div', class_='extra').get_text(strip=True),
            'link': card['href'],
        })
    return anuncios


resposta = buscar(URL_AUTOMOVEIS) #tira a # para rodar
if resposta:
    for anuncio in parsear_anuncios(resposta):
        print(anuncio)