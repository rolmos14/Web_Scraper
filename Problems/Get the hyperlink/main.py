import requests

from bs4 import BeautifulSoup


act, link = [input() for _ in range(2)]
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find('a', {'href': f'#act{act}'}).get('href'))
