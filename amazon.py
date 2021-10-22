import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

affiliate_tag = "rushipatel172-21"
ASIN = "B08XJGNQS7"

for i in range(1,20):
    url = f"https://www.amazon.in/s?k=mobile&page={i}"
    baseurl = "https://www.amazon.in"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    mobile_links = []

    # Find All the Link from a Anchor tag
    links = soup.find_all('a', {'class': 'a-link-normal a-text-normal'}, href=True)
    for item in links:
        link = baseurl + item['href']
        mobile_links.append(link)
        print(baseurl +  item['href'])
        # print("Saving---")

# printing list
# for i in mobile_links:
#     print(i)