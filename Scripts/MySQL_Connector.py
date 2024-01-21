import mysql.connector



#1 - Simple connection with MySQL instance
def mysql_connect(DBhost = "localhost", DBusername = "root", DBpassword = ""):

    try:

        DBConnection = mysql.connector.connect(
            host = DBhost,
            user = DBusername,
            password = DBpassword
        )

        print("\nConnected to MySQL instance successfully!\n")

    except:

        print("\nAn error occured!\n")

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

            print("\nA new database named {nameDB} has been created successfully!\n" .format(nameDB = nameDatabase))

        except:

            print("\n\nAn error occured!\n")


#3 - Connection with fastf1 database
def mysql_connect_fastf1(DBhost = "localhost", DBusername = "root", DBpassword = "", DBname = "fastf1"):

    from Common import yn_input_check

    try:

        DBConnection_fastf1 = mysql.connector.connect(
            host = DBhost,
            user = DBusername,
            password = DBpassword,
            database = DBname
        )

        print("\nConnected to fastf1 database successfully!\n")

    except:

        print("\nNo database named {nameDB} exists in {host}! Would you like to create it now?\n" .format(nameDB = DBname, host = DBhost))

        while(yn_input_check() == False):

            print("\nThe application cannot be executed without a fastf1 database in your MySQL instance! Please, confirm with \"y\" that you want to create a new database named {nameDB}\n" .format(nameDB = DBname))

        mysql_create_database(mysql_connect(DBhost = "localhost", DBusername = "root", DBpassword = ""), "fastf1")

        DBConnection_fastf1 = mysql_connect_fastf1(DBhost = "localhost", DBusername = "root", DBpassword = "", DBname = "fastf1")

    return DBConnection_fastf1


#4 - Drop Database in MySQL instance

def mysql_drop_database(DBConnection, nameDatabase):

    try:

        mySQLcursor = DBConnection.cursor()

        mySQLcursor.execute("DROP DATABASE {nameDB}" .format(nameDB = nameDatabase))

        print("\n\nThe database named {nameDB} has been dropped successfully!\n" .format(nameDB = nameDatabase))

    except:
        
        try:

            DBConnectionTest = mysql.connector.connect(
                host = DBConnection._host,
                username = DBConnection._user,
                password = DBConnection._password,
                database = nameDatabase
            )

        except:

            print("\n\nNo database named {nameDB} exists in {host}!\n" .format(nameDB = nameDatabase, host = DBConnection._host))


#5- Show Databases in MySQL instance

def mysql_show_databases(DBConnection):

    try:

        mySQLcursor = DBConnection.cursor()

        mySQLcursor.execute("SHOW DATABASES")

        for database in mySQLcursor:
            
            print(database)

    except:

        print("\n\nAn error occured!\n")


#6 - Create table in MySQL Database

def mysql_create_table(DBConnection, nameDatabase, nameTable):

    try:

        DBConnectionTest = mysql.connector.connect(
            host = DBConnection._host,
            username = DBConnection._user,
            password = DBConnection._password,
            database = nameDatabase
        )

    except:

        print("\n\nNo database named {nameDB} exists in {host}!\n" .format(nameDB = nameDatabase, host = DBConnection._host))

        try:

            mySQLcursor = DBConnection.cursor()

            mySQLcursor.execute("CREATE TABLE {nameTable}" .format(nameTable = nameTable))

            print("\n\nA new table named {nameTable} has been created successfully in {nameDB}!\n" .format(nameTable = nameTable, nameDB = nameDatabase))

        except:

            print("\n\nAn error occured!\n")


#7 - Drop table in MySQL Database

def mysql_drop_table(DBConnection, nameDatabase, nameTable):

    try:

        mySQLcursor = DBConnection.cursor()

        mySQLcursor.execute("DROP TABLE IF EXISTS {nameTable}" .format(nameDB = nameTable))

        print("\n\nThe Table named {nameTable} has been dropped successfully!\n" .format(nameDB = nameTable))

    except:

        print("\n\nAn error occured!\n")