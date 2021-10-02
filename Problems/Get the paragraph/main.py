import requests

from bs4 import BeautifulSoup


word, link = [input() for _ in range(2)]
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
p_tags = soup.findAll("p")
p_word = next(tag.text for tag in p_tags if word in tag.text)
print(p_word)
