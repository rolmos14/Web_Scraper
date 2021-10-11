import requests
import string
import os

from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self, url, number_of_pages, article_type):
        self.url = url
        self.number_of_pages = number_of_pages
        self.article_type = article_type
        # Force response in English
        self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    def save_articles(self):
        for n in range(1, self.number_of_pages + 1):
            # Create directory for page n and select it as current working directory
            os.chdir("C:\\Users\\ICEMI\\PycharmProjects\\Web Scraper\\Web Scraper\\task")
            os.mkdir(f"Page_{n}")
            os.chdir(f"Page_{n}")
            # Get page n and soup it
            response = requests.get(self.url + f"&page={n}", headers={'Accept-Language': 'en-US,en;q=0.5'})
            soup = BeautifulSoup(response.content, 'html.parser')
            # Loop through all the articles in page n
            for article in soup.findAll("article"):
                # Look for required article type
                if article.find("span", {"class": "c-meta__type"}).text == self.article_type:
                    article_url = self.url[0: self.url.find(".com")] + ".com" + article.find('a').get('href')
                    # Go to article's page and soup it
                    response = requests.get(article_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # Get article title and text
                    article_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
                    article_text = soup.find("div", {"class": "c-article-body u-clearfix"}).text
                    self.save_to_file(article_title, article_text)

    def save_to_file(self, article_title, article_text):
        # Replace punctuation marks and whitespaces with underscores for the file name
        translation_table = str.maketrans(string.punctuation + " ", "_" * (len(string.punctuation) + 1))
        file_name = article_title.translate(translation_table) + ".txt"
        with open(file_name, 'wb') as file:
            # strip() to remove unnecessary whitespaces
            file.write(article_text.strip().encode())
            print("Content saved.")

    def status(self):
        if self.response.status_code != 200:
            print(f"The URL returned {self.response.status_code}")
            return False
        else:
            return True


url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
number_of_pages, article_type = int(input()), input()
web_scraper = WebScraper(url, number_of_pages, article_type)
if web_scraper.status():
    web_scraper.save_articles()
