import unittest
import datetime

class TestCountPeopleSharingBirthday(unittest.TestCase):

    def test_counter(self):     #Generating 3 people, 2 with the same birthday
        
        target = __import__("Stuff.py")

        people = [target.Person(1, datetime.date(2022, 1, 1)), target.Person(2, datetime.date(2022, 1, 1)), target.Person(3, datetime.date(2022, 12, 31))]

        peopleList = [1, 2, 3]

        result = target.count_people_sharing_birthday(people, peopleList)

        self.assertEqual(result, 2)

if __name__ == '__main__':

    unittest.main()