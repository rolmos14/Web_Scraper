import requests

from bs4 import BeautifulSoup


link = input()
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
a_tags = soup.findAll("a")
topics_starting_with_S = [tag.text for tag in a_tags
                          if tag.text.startswith("S") and len(tag.text) > 1
                          and ("entity" in tag.get('href') or "topics" in tag.get('href'))]
print(topics_starting_with_S)
