import json

from MySQL_Connector import mysql_create_database, mysql_create_table, Attribute


#1 - Init fastf1 database

def init_fastf1DB(DBConnection):

    mysql_create_database(DBConnection, "fastf1")

#2 - Init fastf1 tables (TBC)

def init_fastf1Tables(DBConnection):

    with open('MyPythonRepo\Scripts\FastF1_DB\Init_Attribute.json', 'r') as file:
        
        data = json.load(file)
    
    attributeList = [Attribute(attribute["name"], attribute["primary_key"], attribute["data_type"], attribute["not_null"], attribute["auto_increment"]) for attribute in data["attributes"]]
    
    mysql_create_table(DBConnection, "sessions", attributeList)