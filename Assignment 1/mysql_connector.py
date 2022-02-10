import mysql.connector
from mysql.connector import Error
from util import config


config = config()


def fetch(amount):
    query = "SELECT * FROM review LIMIT %s"
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, [amount])
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


def fetch_by_id(id):
    query = "SELECT * FROM review WHERE id = %s"
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, [id])
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


# TODO fix LIKE, no quotes in parameterized query, AsIs returns object, and .format from same library likely has async issues
def fetch_by_site(site, limit=250):
    query = "SELECT * FROM review WHERE url LIKE '%%s%' LIMIT %s"
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, ("%" + site + "%", limit))
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


def fetch_by_contains_word(word, limit):
    query = "SELECT * FROM review WHERE content LIKE '%%s%' LIMIT %s"
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, ("%" + word + "%", limit))
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


def fetch_by_rating(rating):
    query = "SELECT * FROM review WHERE rating = %s"

    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, [rating])
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


def fetch_by_rating_bigger_than(rating):
    query = "SELECT * FROM review WHERE rating > %s"
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, [rating])
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


def fetch_by_rating_smaller_than(rating):
    query = "SELECT * FROM review WHERE rating < %s"

    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, [rating])
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response


def insert_review(**args):
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return
    query = "INSERT INTO url_dump (url,innerText) VALUES (%s, %s)"
    arglist = list()
    arglist.append(args["url"])
    arglist.append(args["innerText"])
    arguments = tuple(arglist)

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, arguments)
            connection.commit()
            cursor.close()
            connection.close()


def insert_review(**args):
    query = "INSERT INTO review (content,author,rating,product,url) VALUES (%s, %s,%s, %s,%s)"
    arglist = list()
    arglist.append(args["content"])
    arglist.append(args["author"])
    arglist.append(args["rating"])
    arglist.append(args["product"])
    arglist.append(args["url"])
    arguments = tuple(arglist)
    if config["username"] == "YOUR_USERNAME_HERE":
        print("PLEASE ENTER PROVIDED USER DETAILS IN config.json")
        return

    try:
        connection = mysql.connector.connect(host=config["host"],
                                             database=config["database"],
                                             user=config["username"],
                                             password=config["password"])
    except Error as err:
        print(err)
    finally:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, arguments)
            connection.commit()
            cursor.close()
            connection.close()
