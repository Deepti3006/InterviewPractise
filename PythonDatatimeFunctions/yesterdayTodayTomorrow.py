import datetime
def yesterdayTodayTomorrow():

    date_today = datetime.datetime.today().date()
    print(date_today)
    date_yesterday = date_today - datetime.timedelta(1)
    print(date_yesterday)
    date_tomorrow = date_today +datetime.timedelta(1)
    print(date_tomorrow)

    for i in range(1,5):
        print(date_today + datetime.timedelta(i))

yesterdayTodayTomorrow()
