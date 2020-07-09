import datetime

def convertDatePattern():

    date_object = datetime.datetime.strptime("Jan 1 2014 2:43PM",'%b %d %Y %I:%M%p')
    print(date_object)

convertDatePattern()

