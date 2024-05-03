import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = 'https://www.bseindia.com/corporates/ann.html'
response = requests.get(url)
print(response)
# parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# find all links on the page
links = soup.find_all('a')

# print the href attribute of each link
for link in links:
    print(link.get('href'))