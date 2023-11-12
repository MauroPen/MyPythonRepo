from Common import yn_input_check, int_input_check, DataframeExport, export_dataframes

from FastF1_DB.Import import import_calendars, import_sessions
from MySQL_Connector import mysql_connect, mysql_create_database, mysql_drop_database, mysql_show_databases

running = True
mainMenu = True

# Init

while(running):

    print("\nWelcome! Do you want to use default authentication settings?\n")

    if (yn_input_check()):

        DBConnection = mysql_connect()

    else:

        print("\nWelcome! Please enter the hostname of your DB:\n")

        hostName = input()

        print("\nGreat, please now enter your username:\n")

        username = input()

        print("\nFine, please now enter your password:\n")

        password = input()

        print("\nAttempting to connect to your database, please wait...\n")

        DBConnection = mysql_connect(hostName, username, password)

    print("\nA list of the databases found in your MySQL instance is following:\n")

    mysql_show_databases(DBConnection)
    
    while(mainMenu):
    
        print("\nWhat do you want to do? Please, input a number from 1 to 5:\n\n1 - Create a new database\n\n2 - Drop a database\n\n3 - Show databases\n\n4 - Import FastF1 data (TBD)\n\n5 - Exit\n")
        
        match int_input_check():

            case 1:                                                     #Create a new database

                print("\nPlease, input the name of the new database:\n")

                nameDatabase = input()

                mysql_create_database(DBConnection, nameDatabase)

            case 2:                                                     #Drop a database

                mysql_show_databases(DBConnection)
                
                print("\nPlease, input the name of the database that you want to drop:\n")

                nameDatabaseDrop = input()

                mysql_drop_database(DBConnection, nameDatabaseDrop)

            case 3:                                                     #Show databases

                mysql_show_databases(DBConnection)

            case 4:                                                     #Insert data

                print("\nIn development!\n")

            case 5:                                                     #Exit main menu

                mainMenu = False
                
                running = False
            
            case _:

                print("\nYour selection is not valid, please enter a valid number.\n")

    """

    # Test import_calendars

    importCalendars = import_calendars(fromYear = 1950, toYear = 1951)

    calendarExport = DataframeExport(importCalendars, "Schedule", False)

    export_dataframes([calendarExport], "Schedule")

    # Test import races

    importSessions = import_sessions(fromYear = 1950, toYear = 1951, importPractice = False, importQualifying = False)

    sessionsExport = DataframeExport(importSessions, "Sessions", False)

    export_dataframes([sessionsExport], "Sessions")

    """