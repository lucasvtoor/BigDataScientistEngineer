import requests
from bs4 import BeautifulSoup
from mysql_connector import insert_review


def start():
    r = requests.get(
        "https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AED6AEB"
        "-AECiAIBqAIDuAL56pGQBsACAdICJDcxODQyNDEwLWI4ZGItNDEzYy04NjhkLTg0YjE3YWE1MDQwONgCBOACAQ;sid"
        "=ffd7ca868d6d04275c7091b539c7a70b;dest_id=-2140479;dest_type=city&/")
    bs = BeautifulSoup(r.content, features="html.parser")
    search_by_tag(bs, "div")


def search_by_tag(ctx, tag):
    x = ctx.findAll(tag)
    for l in x:
        print("------------")
        print(l)
