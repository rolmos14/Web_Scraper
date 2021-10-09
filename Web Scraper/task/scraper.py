import requests


class WebScraper:

    def __init__(self, url):
        self.url = url
        # Force response in English
        self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    def status(self):
        if self.response.status_code != 200:
            print(f"The URL returned {self.response.status_code}")
            return False
        else:
            return True

    def save_to_file(self, file_name):
        with open(file_name, 'wb') as file:
            file.write(self.response.content)
            print("Content saved.")


web_scraper = WebScraper(input("Input the URL:\n"))
if web_scraper.status():
    web_scraper.save_to_file("source.html")
