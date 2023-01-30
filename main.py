import os
from datetime import date, datetime
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
        getQuery()
    except:
        print("Nie można utworzyć takiej bazy")
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


def importDatabase(fileName):
    with open(f"{fileName.lower().replace(';', '')}.sql", "r") as importer:
        test=importer.readlines()
        test2=""
        createDatabase(test2.join(test))


# FUNCTIONS #

def querySwitchCase(query):
    # splitedQuery = query.split()

    if query.split()[0] in possibleQueries:
        if query.split()[0] == possibleQueries[0]:
            createDatabase(query)
        elif query.split()[0] == possibleQueries[1]:
            selectDatabase(query)
        elif query.split()[0] == possibleQueries[2]:
            print('tu bedzie alter')
        elif query.split()[0] == possibleQueries[3]:
            dropDatabase(query)
        elif query.split()[0] == possibleQueries[4]:
            selectQuery(query)
        elif query.split()[0] == possibleQueries[6]:
            showDatabases()
        elif query.split()[0] == possibleQueries[7]:
            print("tu bedzie describe")
        elif query.split()[0] == possibleQueries[8]:
            importDatabase(query.split()[1])
        else:
            print("Nie ma takiej kwerendy")
            getQuery()


# MAIN #

def getQuery():
    print("\nSQL Query:")
    query = input()
    if ";" not in query[-1]:
        query += ";"

    with open(f"queries{date.today()}.txt", "a") as writer:
        # with open("queries.txt", "a") as writer, open("queries.txt", "r") as reader:
        writer.write(str(datetime.now()) + "\ n")
        writer.write(query + "\n\n")
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
