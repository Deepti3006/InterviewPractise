import datetime
def currentTime():

    time_object = datetime.datetime.now().time()
    print(time_object)
currentTime()