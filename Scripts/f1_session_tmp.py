from pandas import DataFrame
from numpy import append

from Common import DataframeExport, export_dataframes 

import fastf1

fastf1.Cache.enable_cache("C:/Users/maupe/Desktop/FastF1_Cache")

dataframes = []

for i in range(1, 23, 1):

    try:
        GP = fastf1.get_session(1950, i, "Race")

        GP.load()

        GPExport = DataframeExport(GP.results, "{number}" .format(number = i), False)

        dataframes = append(dataframes, GPExport)
    
    except ValueError:

        print("All data from 1950 has been retrieved!\n")

    except:

        print("Another error occured!\n")

export_dataframes(dataframes, "Sessions")
