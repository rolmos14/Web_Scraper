import requests

from bs4 import BeautifulSoup


index, link = [input() for _ in range(2)]
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.findAll("h2")[int(index)].text)
