import requests


url = input("Input the URL:\n")
try:
    response = requests.get(url).json()
    print("\n" + response["content"])
except Exception:
    print("\nInvalid quote resource!")
