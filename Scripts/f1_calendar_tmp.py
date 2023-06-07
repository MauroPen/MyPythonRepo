from pandas import DataFrame, concat
from numpy import append

from Common import DataframeExport, export_dataframes 

import fastf1

fastf1.Cache.enable_cache("C:/Users/maupe/Desktop/FastF1_Cache")

schema = DataFrame(columns = list(fastf1.get_event_schedule(1950, include_testing = False).columns))

for year in range(1950, 2024, 1):

    print(" Retrieving calendar schedule from {Year}" .format(Year = year), end = '\r')

    try:

        calendar = fastf1.get_event_schedule(year, include_testing = False)    # Excluding testing session to allow easy referencing

        schema = concat([schema, calendar], ignore_index = True)

    except:

        print("\n\nAn error occured!\n")

schema.insert(0, "ChampionshipYear", schema["EventDate"].dt.year)

calendarExport = DataframeExport(schema, "Schedule", False)

export_dataframes([calendarExport], "Schedule")