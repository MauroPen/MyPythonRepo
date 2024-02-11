from pandas import DataFrame, concat
from numpy import append
from os import getcwd 

import warnings
import fastf1

#1 - Import calendars

def import_calendars(fromYear = 1950, toYear = 2023, cachePath = ''):

    if (cachePath == ''):
        
        cachePath = fastf1.Cache.enable_cache(getcwd())

    schema = DataFrame(columns = list(fastf1.get_event_schedule(fromYear, include_testing = False).columns))

    for year in range(fromYear, toYear + 1, 1):

        print(" Retrieving calendar from {Year}" .format(Year = year), end = '\r')

        try:

            calendars = fastf1.get_event_schedule(year, include_testing = False)    # Excluding testing session to allow easy referencing

            schema = concat([schema, calendars], ignore_index = True)

        except:

            print("\n\nAn error occured!\n")

    schema.insert(0, "ChampionshipYear", schema["EventDate"].dt.year)

    return schema

#2 - Import events --> TO BE FIXED (output is not a DataFrame)

def import_events(fromYear = 1950, toYear = 2023, cachePath = ''):

    if cachePath == '':
        
        cachePath = fastf1.Cache.enable_cache(getcwd())

    schema = DataFrame(columns = list(fastf1.get_event(fromYear, 1).columns))

    for year in range(fromYear, toYear + 1, 1):

        print(" Retrieving events from {Year}" .format(Year = year), end = '\r')

        calendar = fastf1.get_event_schedule(year, include_testing = False)

        for round in range(1, max(calendar["RoundNumber"]), 1):

            events = fastf1.get_event(year, round)

            schema = concat([schema, events], ignore_index = True)

    return schema

#3 - Import sessions

def import_sessions(schema, year, cachePath = '', importPractice = True, importQualifying = True, importRace = True):

    if cachePath == '':
        
        cachePath = fastf1.Cache.enable_cache(getcwd())

    print("\nRetrieving sessions from {Year}" .format(Year = year))

    calendar = fastf1.get_event_schedule(year, include_testing = False)

    for round in range(1, max(calendar["RoundNumber"]), 1):

        if (importPractice):

            session_practice1 = fastf1.get_session(year, round, "FP1")
                
            session_practice2 = fastf1.get_session(year, round, "FP2")
                
            session_practice3 = fastf1.get_session(year, round, "FP3")

            session_practice1.load()

            session_practice2.load()

            session_practice3.load()

            session_practice1.results.insert(0, "Session", "FP1")       #To be substituted with eventId (?)

            session_practice1.results.insert(0, "RoundNumber", round)

            session_practice1.results.insert(0, "ChampionshipYear", year)

            session_practice2.results.insert(0, "Session", "FP2")       #To be substituted with eventId (?)

            session_practice2.results.insert(0, "RoundNumber", round)

            session_practice2.results.insert(0, "ChampionshipYear", year)

            session_practice3.results.insert(0, "Session", "FP3")       #To be substituted with eventId (?)

            session_practice3.results.insert(0, "RoundNumber", round)

            session_practice3.results.insert(0, "ChampionshipYear", year)

            schema = concat([schema, session_practice1.results, session_practice2.results, session_practice3.results], ignore_index = True)

        if (importQualifying):      #To be investigated from when results are available
            
            session_qualifying = fastf1.get_session(year, round, "Qualifying")

            session_qualifying.load()

            session_qualifying.results.insert(0, "Session", "Qualifying")       #To be substituted with eventId (?)

            session_qualifying.results.insert(0, "RoundNumber", round)

            session_qualifying.results.insert(0, "ChampionshipYear", year)

            schema = concat([schema, session_qualifying.results], ignore_index = True)

        if (importRace):
                
            fastf1.logger.set_log_level("ERROR")

            warnings.filterwarnings("ignore", category=FutureWarning)
            
            session_race = fastf1.get_session(year, round, "Race")

            session_race.load()

            session_race.results.insert(0, "Session", "Race")       #To be substituted with eventId (?)

            session_race.results.insert(0, "RoundNumber", round)

            session_race.results.insert(0, "ChampionshipYear", year)

            schema = concat([schema, session_race.results], ignore_index = True)

    return schema
