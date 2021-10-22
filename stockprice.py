import requests
from bs4 import BeautifulSoup

def getData(symbol):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.title.text)

    stock = {
        'price' : soup.find('div', {'class' : 'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'change' : soup.find('div', {'class' : 'D(ib) Mend(20px)'}).find_all('span')[1].text
    }
    return stock
    # print(stock['price'], stock['change'])
print(getData('CL'))