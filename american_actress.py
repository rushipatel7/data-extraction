from typing import List
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def american_Actress(url):
    global nickname, birthplace, occupation, education, yearActive
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    base_url ="https://en.wikipedia.org/wiki/"
    allNames = []
    all_data = []
    all_movie_details = []
    final_data = []

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
            r1 = requests.get(base_url + i['ACTRESS NAME'])
            soup1 = BeautifulSoup(r1.content, 'lxml')  
            
            try:
                nickname = soup1.find('div', {'class':'nickname'}).text.strip()
                birthplace = soup1.find('div', {'class': 'birthplace'}).text.strip()
                occupation = soup1.find('div', {'class': 'hlist hlist-separated'}).text.strip()
                film_data = soup1.find('table', {'class': 'wikitable'})
                for tr in film_data.find_all('tr'):
                    cols1 = tr.find_all('td')
                    cols = [ele.text.strip() for ele in cols1]
                    try:
                        movie_year = cols[0]
                        movie_name = cols[1]
                        # print(movie_name)
                    except:
                        cols = ""
                        movie_name =""
                        movie_year =""
                    else:  
                        # print(movie_name)                  
                        movie_details = [movie_year  + "-"  +  movie_name]
                        # all_movie_details.append(movie_details)
                        for i in movie_details:
                            all_movie_details.append(i)
                        # print(movie_details)         
                # print(occupation)
                
            except:
                if nickname == "":
                    nickname = None  
                elif birthplace == "":
                    birthplace = None
                occupation = None
            else:
                datas = {
                    # 'ACTRESS NAME' : i['ACTRESS NAME'],
                    # 'DOB' : i['DOB'],
                    'NICK NAME': nickname,
                    'BIRTH PLACE' : birthplace,
                    'OCCUPATION' : occupation,
                    'MOVIE DETAILS' : all_movie_details
                }
                all_data.append(datas)
                print("Saving Data--", datas)   
            # print(i['ACTRESS NAME']) 
    final_data = allNames + all_data
    df = pd.DataFrame(final_data, columns=['ACTRESS NAME', 'DOB', 'NICK NAME', 'BIRTH PLACE', 'OCCUPATION', 'MOVIE DETAILS'])
    df.to_csv('American_Actress.csv', header=True, index=False)
        
    
american_Actress("https://en.wikipedia.org/wiki/List_of_American_film_actresses")
