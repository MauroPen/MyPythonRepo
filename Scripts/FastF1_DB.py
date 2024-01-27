from Common import yn_input_check, int_input_check, DataframeExport, export_dataframes
from MySQL_Connector import mysql_connect, mysql_drop_database

from FastF1_DB.Dependency import init_fastf1DB, init_fastf1Tables
from FastF1_DB.Import import import_calendars, import_sessions


running = True
mainMenu = True
DBDefaultName = "fastf1"

# Init

while(running):

    print("\nWelcome! Do you want to use default authentication settings?\n")

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

    print("\nAttempting to connect to your {nameDB} database, please wait...\n" .format(nameDB = DBDefaultName))

    try:
    
        DBConnection = mysql_connect(hostName, username, password, DBDefaultName)
    
    except:

        print("\nNo database named {nameDB} exists in {host}! Would you like to create it now?\n" .format(nameDB = DBDefaultName, host = hostName))

        while(yn_input_check() == False):

            print("\nThe application cannot be executed without a fastf1 database in your MySQL instance! Please, confirm with \"y\" that you want to create a new database named {nameDB}\n" .format(nameDB = DBDefaultName))

        init_fastf1DB(DBConnection)

        DBConnection = mysql_connect(hostName, username, password, DBDefaultName)

        init_fastf1Tables(DBConnection)

    while(mainMenu):
    
        print("\nWhat do you want to do? Please, input a number from 1 to 3:\n\n1 - Check F1 data\n\n2 - Quit\n\n3 - Drop fastf1 database and quit\n")
        
        match int_input_check():

            case 1:                                                     #Check data (update, insert)

                print("\nIn development!\n")

            case 2:                                                     #Quit

                print ("\nAre you sure that you want to exit?\n")

                if(yn_input_check()):
                
                    mainMenu = False
                
                    running = False

            case 3:                                                     #Drop fastf1 database and quit

                print ("\nDo you really want to drop fastf1 database and all its data before exit?\n")

                if(yn_input_check()):

                    mysql_drop_database(DBConnection, DBDefaultName)

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