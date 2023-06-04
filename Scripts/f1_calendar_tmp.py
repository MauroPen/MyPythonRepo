from pandas import DataFrame
from numpy import append

from Common import DataframeExport, export_dataframes 

import fastf1

fastf1.Cache.enable_cache("C:/Users/maupe/Desktop/FastF1_Cache")

dataframes = []

for i in range(2010, 2024, 1):

    try:

        calendar = fastf1.get_event_schedule(i)

        calendarExport = DataframeExport(calendar, "{number}" .format(number = i), False)

        dataframes = append(dataframes, calendarExport)

    except:

        print("An error occured!\n")

export_dataframes(dataframes, "Schedule")
