from requests_html import HTMLSession
import requests

s = HTMLSession()

query = 'surat'
url = f'https://www.google.com/search?q=weather+{query}'

headers = {
    'User-Agent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

r = s.get(url=url, headers=headers)

temp = r.html.find('span#wob_tm', first= True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(query, temp, unit, desc)