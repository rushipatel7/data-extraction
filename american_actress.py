import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def american_Actress(url):
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    allNames = []

    for i in soup.findAll('div', {'class': 'div-col'}):
        li = i.findAll('li')
        for i in li:
            try:
                actress_names = i.find('a').text.strip()
                bday = i.find('span', {'class': 'bday'}).text.strip()
            except:
                bday ="None"
            actress_data = {
                    'ACTRESS NAME' : actress_names,
                    'DOB' : bday
                }
            allNames.append(actress_data)

    for i in allNames:
        print(i)
    df = pd.DataFrame(allNames, columns=['ACTRESS NAME', 'DOB'])
    df.to_csv('American_Actress.csv', header=True, index=False)
    
american_Actress("https://en.wikipedia.org/wiki/List_of_American_film_actresses")
