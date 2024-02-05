import mysql.connector

from tabulate import tabulate

#1 - Connection with MySQL instance

def mysql_connect(DBhost = "localhost", DBusername = "root", DBpassword = "", DBName = ""):

    DBConnection = mysql.connector.connect(
        host = DBhost,
        user = DBusername,
        password = DBpassword,
        database = DBName
    )

    print("\nConnected to MySQL instance successfully!\n")

    return DBConnection


#2 - Create Database in MySQL instance (TO BE REFACTORED)

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


#3 - Drop Database in MySQL instance

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


#4 - Show Databases in MySQL instance

def mysql_show_databases(DBConnection):

    mySQLcursor = DBConnection.cursor()

    mySQLcursor.execute("SHOW DATABASES")

    for database in mySQLcursor:
            
        print(database)


#5a - An entity describing an attribute and its properties

class Attribute:

    def __init__(self, Name, Primary_Key, Data_Type, Not_Null, Auto_Increment):       #Must be boolean and strings
        
        self.name = Name
        self.primary_key = Primary_Key
        self.data_type = Data_Type
        self.not_null = Not_Null
        self.auto_increment = Auto_Increment
    
    def __str__(self):
        
        return f"Attribute name: {self.name} (primary_key = {self.primary_key}, data_type = {self.data_type}, not_null = {self.not_null}, auto_increment = {self.auto_increment}"

        
#6 - Create table in MySQL Database

def mysql_create_table(DBConnection, nameTable, attributeList):

    query = "CREATE TABLE {nameTable} (" .format(nameTable = nameTable)

    iteration = 0
            
    for attribute in attributeList:

        iteration += 1

        query = query + str(attribute.name)

        query = query + " " + str(attribute.data_type)

        if (attribute.not_null):

            query = query + " " + "NOT NULL"

        if (attribute.auto_increment):

            query = query + " " + "AUTO_INCREMENT"

        if (attribute.primary_key):

            query = query + " " + "PRIMARY KEY"
                
        if(iteration < len(attributeList)):

            query = query + ", "

        else:

            query = query + ")"

    mySQLcursor = DBConnection.cursor()

    mySQLcursor.execute(query)

    print("\n\nA new table named {nameTable} has been created successfully in {nameDB}!\n" .format(nameTable = nameTable, nameDB = DBConnection.database))

    print("Its attributes are:\n\n")
    
    attributesTable = []

    for attribute in attributeList:

        attributesTable.append([attribute.name, str(attribute.primary_key), attribute.data_type, str(attribute.not_null), str(attribute.auto_increment)])

    print(tabulate(attributesTable, headers = ["Attribute Name", "Data Type", "Primary Key", "Not Null", "Auto Increment"], tablefmt = "github", stralign = "center", showindex = "False"))


#7 - Drop table in MySQL Database

def mysql_drop_table(DBConnection, nameTable):

    mySQLcursor = DBConnection.cursor()

    mySQLcursor.execute("DROP TABLE IF EXISTS {nameTable}" .format(nameDB = nameTable))

    print("\n\nThe Table named {nameTable} has been dropped successfully!\n" .format(nameDB = nameTable))


#8 - Retrieve attributes from existing table as an array of strings

def retrieve_attributes(DBConnection, nameTable):
        
    query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{nameTable}' ORDER BY ORDINAL_POSITION" .format(nameTable = nameTable)
    
    mySQLcursor = DBConnection.cursor()

    mySQLcursor.execute(query)

    myresult = mySQLcursor.fetchall()

    attributeArray = [tup[0] for tup in myresult]     #Extract the first element from each tuple

    return attributeArray

