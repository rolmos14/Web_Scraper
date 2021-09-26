import requests


class WebScraper:

    def __init__(self, url):
        self.url = url

    def print_quote(self):
        response = requests.get(self.url)
        if response.ok and "content" in response.json():
            print("\n" + response.json()["content"])
        else:
            print("\nInvalid quote resource!")


quotable = WebScraper(input("Input the URL:\n"))
quotable.print_quote()
