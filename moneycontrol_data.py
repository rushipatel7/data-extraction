import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# url = 'https://www.moneycontrol.com/stocks/marketstats/bse-gainer/all-companies_-1/'
indianIndexurl = 'https://www.moneycontrol.com/markets/indian-indices/'
# r = requests.get(url=url, headers=headers)

# soup = BeautifulSoup(r.content, 'html.parser')


# shareLinks = []

# company_share_Link = soup.find('tbody')
# print(company_share_Link)



# TOP GAINER DATA FETCH
def topGainer(gainerUrl):
    r = requests.get(url=gainerUrl, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    company_name = soup.find('div', {'class': 'bsr_table hist_tbl_hm'})
    for tr in company_name.find_all('tr'):
        # print(tr.find('span', {'class': 'gld13 disin'}))
        l = [e.findAll('a') for e in tr.find('span', {'class': 'gld13 disin'}) ]
        print(l)

    # print(company_name)
    # for tr in company_name.find_all('td'):
    #     print(tr)
    #     cols1 = tr.find('span', {'class' : 'gld13 disin'})
    #     company_name = tr.find('span', {'class' : 'gld13 disin'})
    #     print(company_name)
        # cols = [ele.text.strip() for ele in cols1]
        # print(cols1[1].text)
topGainer('https://www.moneycontrol.com/stocks/marketstats/bse-gainer/all-companies_-1/more/')




# Find Data From the Table
# sharelink = soup.find('tbody').find_all('a', href=True)
# # company_name = soup.find('span', {'class' : 'gld13 disin'}).find_all('a')[0].text
# high = soup.find('tbody').find_all('td')[1].text
# low = soup.find('tbody').find_all('td')[2].text
# lastPrice = soup.find('tbody').find_all('td')[3].text
# prevClose = soup.find('tbody').find_all('td')[4].text
# change = soup.find('tbody').find_all('td')[5].text
# percentGain = soup.find('tbody').find_all('td')[6].text
# print(sharelink, high, low, lastPrice, prevClose, change, percentGain)








# Indian market fetch
# Fetch the table data (INDIAN INDICIS)

def indianIndex(indianIndexUrl):
    r = requests.get(url=indianIndexUrl, headers=headers)
    soup =BeautifulSoup(r.content, 'html.parser')
    stockDataList = []
    company_name = soup.find('tbody')
    for tr in company_name.find_all('tr'):
        cols1 = tr.find_all('td')
        cols = [ele.text.strip() for ele in cols1]

        # print(cols)

        links = [a.findAll('a') for a in cols1]
        # print(links[0][0]['href'])
        # shareLinks = links[0][0]['href']
    
        stockData = {
            'SHARE LINK' : links[0][0]['href'],
            'SHARE NAME' : cols[0],
            'LTP' : cols[1],
            '% CHANGE' : cols[2],
            'VOLUME' : cols[3],
            'BUY PRICE' : cols[4],
            'SELL PRICE' : cols[5],
            'BUY QTY' : cols[6],
            'SELL QTY' : cols[7]
        }
        stockDataList.append(stockData)
        print("Saving Share Data Entry in CSV File", stockData['SHARE NAME'])

    df = pd.DataFrame(stockDataList, columns=['SHARE LINK', 'SHARE NAME', 'LTP', '% CHANGE', 'VOLUME', 'BUY PRICE', 'SELL PRICE',
                                            'BUY QTY', 'SELL QTY'])
    df.to_csv('moneycontrol_data.csv', encoding='utf-8', header=True, index=False)

# indianIndex(indianIndexUrl=indianIndexurl)