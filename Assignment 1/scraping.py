import requests
from bs4 import BeautifulSoup


def start():
    print("test")
    r = requests.get("https://www.booking.com/")
    print(r.content)
    bs = BeautifulSoup(r.content, features="html.parser")
