import os
import mysql.connector
from privateVariables import *
from variables import *

connection = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOSTNAME)
cursor = connection.cursor()


# MYSQL #

def showDatabases():
    cursor.execute("SHOW DATABASES;")
    print("-" * 9, "SCHEMAS", "-" * 9)
    for databases in cursor:
        print(*databases)
    getQuery()


def selectDatabase(use):
    cursor.execute(use)
    cursor.execute("SHOW TABLES;")
    print("-" * 9, "TABLES", "-" * 9)
    for tables in cursor:
        print(*tables)
    getQuery()


def createDatabase(create):
    test = create.split()
    try:
        cursor.execute(create)
        print(f"Pomyślnie utworzono bazę {test[::0]}")
    except:
        print("Nie można utworzyć takiej bazy")
        main()
    getQuery()


def dropDatabase(drop):
    test = drop.split()
    try:
        cursor.execute(drop)
        print(f"Pomyślnie usunięto bazę {test[-1]}")
        main()
    except:
        print("Nie ma w zbiorze takiej bazy")
        main()


def selectQuery(select):
    splitedQuery = select.split()
    test = splitedQuery.index("FROM")

    print("\n")

    cursor.execute(f"DESCRIBE {splitedQuery[test + 1]}")
    for columnName in cursor:
        print("|", columnName[0], end=" |   ")

    print("\n")

    cursor.execute(select)
    for row in cursor:
        for i in range(len(row)):
            print("|", row[i], end=" |   ")
        print("\n")

    getQuery()


# FUNCTIONS #

def querySwitchCase(query):
    splitedQuery = query.split()

    if splitedQuery[0] in possibleQueries:
        if splitedQuery[0] == possibleQueries[0]:
            createDatabase(query)
        elif splitedQuery[0] == possibleQueries[1]:
            selectDatabase(query)
        elif splitedQuery[0] == possibleQueries[2]:
            print('tu bedzie alter')
        elif splitedQuery[0] == possibleQueries[3]:
            dropDatabase(query)
        elif splitedQuery[0] == possibleQueries[4]:
            selectQuery(query)
        elif splitedQuery[0] == possibleQueries[5]:
            showDatabases()
        elif splitedQuery[0] == possibleQueries[6]:
            print("tu bedzie describe")
        else:
            print("Nie ma takiej kwerendy")
            getQuery()


# MAIN #

def getQuery():
    print("\nSQL Query:")
    query = input()
    if ";" not in query[-1]:
        query += ";"
    querySwitchCase(query.upper())


def main():
    os.system('cls')
    print("=" * 52)
    print("=" * 11, "MySQL Workbench by mitthunder", "=" * 10)
    print("=" * 23, "v0.1", "=" * 23)
    print("=" * 52, "\n\n")

    showDatabases()
    getQuery()


main()
