import mysql_connector as mc
from scraping import start
from alt_scraping import search_booking


def main():
    # insert(content="Very bueno", author="me", rating=5, product="Wild thing", url="amazon")
    # print(fetch(2))
    # print(fetchById(2))
    # print(fetchBySite(str("me"), 2))
    # print(fetchByRating(5))
    search_booking("Amsterdam", 2022, 3, 2, 2022, 3, 8, 2, 5, [16, 18])


if __name__ == "__main__":
    main()
