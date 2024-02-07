import json

from MySQL_Connector import mysql_create_database, mysql_create_table, Attribute, mysql_insert
from FastF1_DB.Import import import_sessions


#1 - Init fastf1 database

def init_fastf1DB(DBConnection):

    mysql_create_database(DBConnection, "fastf1")

#2 - Init fastf1 tables

def init_fastf1Tables(DBConnection):

    with open('MyPythonRepo\Scripts\FastF1_DB\Init_Attribute.json', 'r') as file:
        
        data = json.load(file)
    
    attributesList = [Attribute(attribute["name"], attribute["primary_key"], attribute["data_type"], attribute["not_null"], attribute["auto_increment"]) for attribute in data["attributes"]]
    
    mysql_create_table(DBConnection, "sessions", attributesList)

#3 - Insert rows into "sessions" table

def init_fastf1_sessions(DBConnection, fromYear = 1950, toYear = 1950, importPractice = False, importQualifying = False):

    importSessions = import_sessions(fromYear, toYear, importPractice, importQualifying)

    # Data type conversions

    importSessions["Position"] = importSessions["Position"].astype(int)

    importSessions["GridPosition"] = importSessions["GridPosition"].astype(int)

    importSessions["Q1"] = importSessions["Q1"].astype(str)

    importSessions["Q2"] = importSessions["Q2"].astype(str)

    importSessions["Q3"] = importSessions["Q3"].astype(str)

    importSessions["Time"] = importSessions["Time"].astype(str)

    importSessions["Points"] = importSessions["Points"].astype(int)

    # Increase by one the indices of the DataFrame

    importSessions.index += 1

    # Iterate on DataFrame rows using itertuples and including indices

    sessionsTuples = [tuple(row[0:20]) for row in importSessions.itertuples()]

    mysql_insert(DBConnection, "sessions", sessionsTuples)