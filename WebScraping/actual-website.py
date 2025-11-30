from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/chart/top/?ref_=hm_nv_menu').text

soup = BeautifulSoup(source, 'lxml')


html = soup.find('html')

print(html)

