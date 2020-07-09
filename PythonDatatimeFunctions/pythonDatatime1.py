import datetime

def displayDates():
    print("Current Time of the day :", datetime.datetime.now())
    print("current year of the date:", datetime.datetime.today().strftime("%Y"))
    print("current month of the date", datetime.datetime.today().strftime("%M"))
    print("current week number of the year:", datetime.datetime.today().strftime("%W"))
    print("current week day of the week :", datetime.datetime.today().strftime("%w"))
    print("current day of the year:", datetime.datetime.today().strftime("%j"))
    print("current day of the month:", datetime.datetime.today().strftime("%d"))
    print("current weekday of the month:", datetime.datetime.today().strftime("%A"))
    
displayDates()