import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=books&_sacat=184644&Publication%2520Year=2010%252DNow&_dcat=184644&LH_BIN=1&_pgn=1&rt=nc'


# get the ebay site listings
response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

# create links for pagenation
links = []
for i in range(1, 50):
    links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=books&_sacat=184644&Publication%2520Year=2010'
                 '%252DNow&_dcat=184644&LH_BIN=1&_pgn'+str(i)+'&rt=nc') 

price_list = []
url_list = []
book_titles = []

for link in links:
    response = requests.get(link)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    prices = html_soup.findAll('span', class_='s-item__price')
    titles = html_soup.findAll('h3', class_='s-item__title')
    urls = html_soup.findAll('a', class_='s-item__link')
    for i in range(1, len(prices)):
        price_list.append(prices[i].text)
    for i in range(1, len(titles)):
        book_titles.append(titles[i].text)
    for i in range(1, len(urls)):
        url_list.append(urls[i]['href'])
print(len(url_list))
print(len(book_titles))
print(len(price_list))


df_url = pd.DataFrame(list(zip(url_list, book_titles, price_list)), columns=['url', 'titles', 'prices'])
