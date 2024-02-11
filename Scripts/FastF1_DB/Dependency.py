import json
from pandas import DataFrame, Timedelta

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

    schema = DataFrame(columns = ['ChampionshipYear', 'RoundNumber', 'Session', 'DriverNumber', 'BroadcastName', 'Abbreviation', 'TeamName',
       'TeamColor', 'FirstName', 'LastName', 'FullName', 'Position',
       'GridPosition', 'Q1', 'Q2', 'Q3', 'Time', 'Status', 'Points'])
    
    year = fromYear
    
    while (year <= toYear):
  
        importSessions = import_sessions(schema, year, importPractice = importPractice, importQualifying = importQualifying)
        
        # Managing NULL values and data type conversions

        importSessions["Position"] = importSessions["Position"].astype(str)

        importSessions["GridPosition"] = importSessions["GridPosition"].astype(str)

        importSessions["Q1"] = importSessions["Q1"].astype(str)

        importSessions["Q2"] = importSessions["Q2"].astype(str)

        importSessions["Q3"] = importSessions["Q3"].astype(str)
    
        importSessions["Time"] = importSessions["Time"].fillna(Timedelta(seconds = 0))

        importSessions["Time"] = importSessions["Time"].dt.total_seconds()

        importSessions["Points"] = importSessions["Points"].astype(int)

        # Iterate on DataFrame rows using itertuples and including indices

        sessionsTuples = [tuple(row[1:20]) for row in importSessions.itertuples()]

        mysql_insert(DBConnection, "sessions", sessionsTuples)

        year += 1