from mysql_connector import fetch, insert, fetchById, fetchBySite,fetchByRatingSmallerThan,fetchByRatingBiggerThan,fetchByRating


def main():
    # insert(content="Very bueno", author="me", rating=5, product="Wild thing", url="amazon")
    # print(fetch(2))
    # print(fetchById(2))
    # print(fetchBySite(str("me"), 2))
    print(fetchByRating(5))


if __name__ == "__main__":
    main()
