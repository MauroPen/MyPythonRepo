from unittest import TestCase, main
from numpy import array
from datetime import date

from Scripts.Birthday_Paradox.Dependency import Person, check_people_sharing_birthday, count_people_sharing_birthday       #Valid only when testing scripts with absolute modules (no personal modules)

class TestCheckPeopleSharingBirthday(TestCase):

    def test_check1(self):          #Generating 3 people, none with the same birthday, the first one is always a dummy

        people = [Person(0, date(1900, 1, 1), False),
                  Person(1, date(2022, 1, 1), False),
                  Person(2, date(2022, 6, 15), False),
                  Person(3, date(2022, 12, 31), False)]
        
        peopleTrialArray = array([[0, 0, date(1900, 1, 1), False],
                                  [0, 1, date(2022, 1, 1), False],
                                  [0, 2, date(2022, 6, 15), False],
                                  [0, 3, date(2022, 12, 31), False]])
        
        peopleList = tuple([1, 2, 3])       #Tuples are more efficient than lists

        expectedResult_people = people

        expectedResult_peopleTrialArray = peopleTrialArray

        (result_people, result_peopleTrialArray) = check_people_sharing_birthday(people, peopleTrialArray, peopleList)

        self.assertTrue(((result_people == expectedResult_people)) & ((result_peopleTrialArray == expectedResult_peopleTrialArray).all()), "Test failed! The algorithm has found matching birthdays but there are not.")

    def test_check2(self):          #Generating 3 people, 2 with the same birthday, the first one is always a dummy

        people = [Person(0, date(1900, 1, 1), False),
                  Person(1, date(2022, 1, 1), False),
                  Person(2, date(2022, 1, 1), False),
                  Person(3, date(2022, 12, 31), False)]
        
        peopleTrialArray = array([[0, 0, date(1900, 1, 1), False],
                                  [0, 1, date(2022, 1, 1), False],
                                  [0, 2, date(2022, 1, 1), False],
                                  [0, 3, date(2022, 12, 31), False]])
        
        peopleList = tuple([1, 2, 3])       #Tuples are more efficient than lists

        expectedResult_people = [Person(0, date(1900, 1, 1), False),
                                 Person(1, date(2022, 1, 1), True),
                                 Person(2, date(2022, 1, 1), True),
                                 Person(3, date(2022, 12, 31), False)]

        expectedResult_peopleTrialArray = array([[0, 0, date(1900, 1, 1), False],
                                                 [0, 1, date(2022, 1, 1), True],
                                                 [0, 2, date(2022, 1, 1), True],
                                                 [0, 3, date(2022, 12, 31), False]])

        (result_people, result_peopleTrialArray) = check_people_sharing_birthday(people, peopleTrialArray, peopleList)

        self.assertTrue(((result_people[1].birthday_match == expectedResult_people[1].birthday_match)) &
                        ((result_people[2].birthday_match == expectedResult_people[2].birthday_match)) &
                        ((result_people[3].birthday_match == expectedResult_people[3].birthday_match)) &
                        ((result_peopleTrialArray == expectedResult_peopleTrialArray).all()),
                        "Test failed! The algorithm has not found the right matching birthdays.")

class TestCountPeopleSharingBirthday(TestCase):

    def test_counter1(self):        #Generating 3 people, none with the same birthday ("check" is already done), the first one is always a dummy

        people = [Person(0, date(1900, 1, 1), False),
                  Person(1, date(2022, 1, 1), False),
                  Person(2, date(2022, 6, 15), False),
                  Person(3, date(2022, 12, 31), False)]
        
        peopleList = tuple([1, 2, 3])       #Tuples are more efficient than lists

        result_counter = count_people_sharing_birthday(people, peopleList)

        self.assertEqual(result_counter, 0, "Test failed! Test should have returned 0 but it has returned {Result}." .format(Result = result_counter))

    def test_counter2(self):        #Generating 3 people, 2 with the same birthday ("check" is already done), the first one is always a dummy

        people = [Person(0, date(1900, 1, 1), False),
                  Person(1, date(2022, 1, 1), True),
                  Person(2, date(2022, 1, 1), True),
                  Person(3, date(2022, 12, 31), False)]
        
        peopleList = tuple([1, 2, 3])       #Tuples are more efficient than lists

        result_counter = count_people_sharing_birthday(people, peopleList)

        self.assertEqual(result_counter, 2, "Test failed! Test should have returned 2 but it has returned {Result}." .format(Result = result_counter))

if __name__ == '__main__':

    main()