import requests
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self, url):
        self.url = url
        # Force response in English
        self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def print_title_description(self):
        print()
        if "title" in self.url:
            title = self.soup.find("title").text
            description = self.soup.find("meta", {"name": "description"})["content"]
            print({"title": title, "description": description})
        else:
            print("Invalid movie page!")


quotable = WebScraper(input("Input the URL:\n"))
quotable.print_title_description()
