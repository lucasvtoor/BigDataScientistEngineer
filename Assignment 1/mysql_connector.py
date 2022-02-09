import json
import mysql.connector
from psycopg2.extensions import AsIs
from mysql.connector import Error

with open("config.json") as config_file:
    config = json.load(config_file)


def fetch(amount):
    query = """
        SELECT * FROM review LIMIT %s
    """
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


def fetchById(id):
    query = """
        SELECT * FROM review WHERE id = %s
    """
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
def fetchBySite(site, limit=250):
    query = """
        SELECT * FROM review WHERE url LIKE '%%s%' LIMIT %s
    """
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
            cursor.execute(query, (AsIs(site).__conform__(), limit))
            response = cursor.fetchall()
            cursor.close()
            connection.close()
            return response
#     def fetchByContainsWord(word):

def fetchByRating(rating):
    query = """
        SELECT * FROM review WHERE rating = %s
    """
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


def fetchByRatingBiggerThan(rating):
    query = """
            SELECT * FROM review WHERE rating > %s
        """
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


def fetchByRatingSmallerThan(rating):
    query = """
                 SELECT * FROM review WHERE rating < %s
             """
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


def insert(**args):
    query = """
    INSERT INTO review (content,author,rating,product,url) VALUES (%s, %s,%s, %s,%s)
    """
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
