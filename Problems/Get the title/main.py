import requests

from bs4 import BeautifulSoup


link = input()
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("h1").text)
