import datetime


def calcdaytime():
    curr_day = datetime.date.today() -datetime.timedelta(5)
    print(curr_day)
calcdaytime()