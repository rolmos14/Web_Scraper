import requests
import string

from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self, url):
        self.url = url
        # Force response in English
        self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def save_news(self):
        # Loop through all the articles
        for article in self.soup.findAll("article"):
            # Look for News type
            if article.find("span", {"class": "c-meta__type"}).text == "News":
                article_url = "https://www.nature.com" + article.find('a').get('href')
                # Go to article's page
                response = requests.get(article_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
                soup = BeautifulSoup(response.content, 'html.parser')
                # Get article title and text
                article_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
                article_text = soup.find("div", {"class": "c-article-body u-clearfix"}).text
                self.save_to_file(article_title, article_text)

    def status(self):
        if self.response.status_code != 200:
            print(f"The URL returned {self.response.status_code}")
            return False
        else:
            return True

    def save_to_file(self, article_title, article_text):
        translation_table = str.maketrans(string.punctuation + " ", "_" * (len(string.punctuation) + 1))
        file_name = article_title.translate(translation_table) + ".txt"
        with open(file_name, 'wb') as file:
            file.write(bytes(article_text, encoding="utf-8"))
            print("Content saved.")


web_scraper = WebScraper("https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3")
if web_scraper.status():
    web_scraper.save_news()
