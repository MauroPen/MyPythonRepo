import unittest
import datetime

from Scripts import Common as C #Valid only when testing scripts with global variables (no personal modules)

class TestCountPeopleSharingBirthday(unittest.TestCase):

    def test_counter(self):     #Generating 3 people, 2 with the same birthday, the first one is always a dummy

        people = [C.Person(0, datetime.date(1900, 1, 1), False), C.Person(1, datetime.date(2022, 1, 1), True), C.Person(2, datetime.date(2022, 1, 1), True), C.Person(3, datetime.date(2022, 12, 31), False)]
        peopleList = [1, 2, 3]

        result = C.count_people_sharing_birthday(people, peopleList)

        self.assertEqual(result, 2)

if __name__ == '__main__':

    unittest.main()