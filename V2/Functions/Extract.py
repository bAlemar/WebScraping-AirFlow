import requests
from bs4 import BeautifulSoup


def webscraping_buscape(**kwargs):
    #Extração
    url = 'https://www.buscape.com.br/search?q=placa%20de%20video%20rtx%203060&hitsPerPage=24&prx=true&page=1&sortBy=price_asc&isDealsPage=false&enableRefinementsSuggestions=true'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    Top_5_menor_Preco = soup.find_all('p',{'data-testid': 'product-card::price'})[:5]
    print(Top_5_menor_Preco)    
    return Top_5_menor_Preco