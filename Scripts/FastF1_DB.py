from Common import DataframeExport, export_dataframes

from FastF1_DB.Import import import_calendars, import_sessions

# Test import_calendars

importCalendars = import_calendars(fromYear = 1950, toYear = 1951)

calendarExport = DataframeExport(importCalendars, "Schedule", False)

export_dataframes([calendarExport], "Schedule")



importSessions = import_sessions(fromYear = 1950, toYear = 1951, importPractice = False, importQualifying = False)

sessionsExport = DataframeExport(importSessions, "Sessions", False)

export_dataframes([sessionsExport], "Sessions")