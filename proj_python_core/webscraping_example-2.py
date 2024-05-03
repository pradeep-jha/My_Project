import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

url = "https://www.bseindia.com/corporates/ann.html"

soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = soup.find_all('div',attrs={'class':'track-info track'})

for i, element in enumerate(data):
    for link in element.find_all('div',attrs={'class':'waveform before'}):
        print(str(i) + '- ' + element.find('a').text)
        print('\t' + link['data-url'])