from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
   
# match = soup.title.text
# match = soup.div

# match = soup.find('div', class_='footer')
for article in soup.find_all('div', class_='article'):
    headline = article.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()










