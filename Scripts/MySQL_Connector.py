import mysql.connector

#1 - Simple connection with MySQL instance
def mysql_connect(DBhost = "localhost", DBusername = "root", DBpassword = ""):

    try:

        DBConnection = mysql.connector.connect(
            host = DBhost,
            user = DBusername,
            password = DBpassword
        )

        print("\n\n Connected to MySQL instance successfully!\n")

    except:

        print("\n\nAn error occured!\n")

    return DBConnection

#2 - Create Database in MySQL instance

def mysql_create_database(DBConnection, nameDatabase):

    try:

        DBConnectionTest = mysql.connector.connect(
            host = DBConnection._host,
            username = DBConnection._user,
            password = DBConnection._password,
            database = nameDatabase
        )

        print("\n\n A database named {nameDB} already exists in {host}!\n" .format(nameDB = nameDatabase, host = DBConnection.host))

    except:

        try:

            mySQLcursor = DBConnection.cursor()

            mySQLcursor.execute("CREATE DATABASE {nameDB}" .format(nameDB = nameDatabase))

            print("\n\n A new database named {nameDB} has been created successfully!\n" .format(nameDB = nameDatabase))

        except:

            print("\n\nAn error occured!\n")


#3- Drop Database in MySQL instance

def mysql_drop_database(DBConnection, nameDatabase):

    try:

        DBConnectionTest = mysql.connector.connect(
            host = DBConnection._host,
            username = DBConnection._user,
            password = DBConnection._password,
            database = nameDatabase
        )

    except:

        print("\n\n No database named {nameDB} exists in {host}!\n" .format(nameDB = nameDatabase, host = DBConnection.host))

    try:

        mySQLcursor = DBConnection.cursor()

        mySQLcursor.execute("DROP DATABASE {nameDB}" .format(nameDB = nameDatabase))

        print("\n\n The database named {nameDB} has been dropped successfully!\n" .format(nameDB = nameDatabase))

    except:

        print("\n\nAn error occured!\n")
