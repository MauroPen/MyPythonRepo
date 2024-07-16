from Common import yn_input_check, int_input_check, DataframeExport, export_dataframes
from MySQL_Connector import mysql_connect, mysql_create_database, mysql_drop_database

from FastF1_DB.Dependency import init_fastf1DB, init_fastf1Tables, init_fastf1_sessions, init_fastf1_database
from FastF1_DB.Import import import_calendars, import_sessions

running = True
mainMenu = True
dummyDBName = "fastf1_dump"
defaultFromYear = 2021
defaultToYear = 2023

# App Start

while(running):

    print("\nWelcome! To create a dump file, a MySQL instance is required. Do you want to use default authentication settings?\n")

    if (yn_input_check()):

        print("\nAttempting to connect to your MySQL instance, please wait...\n")

        try:
        
            DBConnection = mysql_connect()

            [hostName, username, password] = [DBConnection._host, DBConnection._user, DBConnection._password]

        except:

            print("\nAn error occured!\n")

            mainMenu = False

            running = False

            break

    else:

        print("\nWelcome! Please enter the hostname of your DB:\n")

        hostName = input()

        print("\nGreat, please now enter your username:\n")

        username = input()

        print("\nFine, please now enter your password:\n")

        password = input()

        print("\nAttempting to connect to your MySQL instance, please wait...\n")

        try:
        
            DBConnection = mysql_connect(hostName, username, password)
        
        except:

            print("\nAn error occured!\n")

            mainMenu = False

            running = False

            break
    
    print("\nWould you like to use default settings?\n")

    if (yn_input_check()):

        (fromYear, toYear) = (defaultFromYear, defaultToYear)

    else:

        print("\nFrom which year would you like to export data?\n")

        fromYear = int_input_check()

        print("\nUntil which year would you like to export data?\n")

        toYear = int_input_check()

    print("\nThe program will now start to generate the dump file.\n Please, notice that during the process a dummy database named {nameDB} will be used and eventually removed.\n" .format(nameDB = dummyDBName))

    mysql_create_database(DBConnection, dummyDBName)

    DBConnection = mysql_connect(hostName, username, password, dummyDBName)

    init_fastf1Tables(DBConnection)

    print("\n\nYour fastf1 Database is going to be populated with the results of races from {fromYear} to {toYear}. The operation may take some minutes.\n" .format(fromYear = fromYear, toYear = toYear))

    init_fastf1_sessions(DBConnection, fromYear, toYear, importPractice = False, importQualifying = False)
    
    print("\nDump DB has been successfully created!\n")

    running = False