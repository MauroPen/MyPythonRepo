import json

from MySQL_Connector import mysql_create_database, mysql_create_table, Attribute


#1 - Init fastf1 database

def init_fastf1DB(DBConnection):

    mysql_create_database(DBConnection, "fastf1")

#2 - Init fastf1 tables (TBC)

def init_fastf1Tables(DBConnection):
    
    attributeList = [Attribute("id", True, "INT", True, True)]
    
    mysql_create_table(DBConnection, "Prova_Table", attributeList)