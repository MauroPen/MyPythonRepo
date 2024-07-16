from unittest import TestCase, main
import mysql.connector

from Scripts.MySQL_Connector import mysql_connect, mysql_create_database, mysql_drop_database

class TestSimpleConnection(TestCase):

    def test_connection(self):

        DBhost, DBusername, DBpassword = ["localhost", "root", ""]
        
        DBConnection = mysql_connect()
        
        DBConnectionTest = mysql.connector.connect(
            host = DBhost,
            user = DBusername,
            password = DBpassword
        )
        
        self.assertTrue(((DBConnection._host == DBConnectionTest._host) & 
                         (DBConnection._user == DBConnectionTest._user) &
                         (DBConnection._password == DBConnectionTest._password)),

                         "The connection to the MySQL instance failed!"
        )

class TestCreateDatabase(TestCase):

    def test_create_new_database(self):

        DBConnection = mysql_connect()

        mysql_create_database(DBConnection, "test")

        DBConnectionTest = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "test"
        )
    
        self.assertTrue(DBConnectionTest._database == "test", "No new database has been created!")

        mysql_drop_database(DBConnection, "test")

if __name__ == '__main__':

    main()