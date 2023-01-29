import os
import mysql.connector
from variables import *

connection = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOSTNAME)
cursor = connection.cursor()


# MYSQL #

def showDatabases():
    cursor.execute("SHOW DATABASES;")
    print("-" * 9, "SCHEMAS", "-" * 9)
    for databases in cursor:
        print(*databases)
    # print("\nCzy chcesz wybrać jakąś bazę?")
    # selection = input()
    # selectionSwitchCase(selection)


def selectDatabase():
    print("\nPodaj jaką bazę chcesz wybrać")
    database = input()
    cursor.execute(f"USE {database};")
    cursor.execute("SHOW TABLES;")
    print("-" * 9, "TABLES", "-" * 9)
    for tables in cursor:
        print(*tables)


def createDatabase():
    print("Jak chcesz nazwać bazę?")
    databaseName = input()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {databaseName};")
        print(f"Pomyślnie utworzono bazę {databaseName}")
        main()
    except:
        print("Nie ma w zbiorze takiej bazy")
        main()


def dropDatabase():
    print("Jaką bazę chcesz usunąć?")
    databaseName = input()
    try:
        cursor.execute("DROP DATABASE IF EXISTS {databaseName};")
        print(f"Pomyślnie usunięto bazę {databaseName}")
        main()
    except:
        print("Nie ma w zbiorze takiej bazy")
        main()


# FUNCTIONS #

def querySwitchCase(action):
    if action == 1:
        showDatabases()
    elif action == 2:
        selectDatabase()
    elif action == 3:
        createDatabase()
    elif action == 4:
        dropDatabase()
    else:
        print("Narazie niedotepne")


def selectionSwitchCase(selection):
    if selection.lower() in possibleSelections or selection == 1:
        querySwitchCase(2)
    else:
        main()


# MAIN #

def main():
    os.system('cls')
    print("=" * 52)
    print("=" * 11, "MySQL Workbench by mitthunder", "=" * 10)
    print("=" * 23, "v0.1", "=" * 23)
    print("=" * 52, "\n\n")

    showDatabases()
    selectDatabase()

    print("\nSQL Query:")
    query = input()
    querySwitchCase(query)


main()
