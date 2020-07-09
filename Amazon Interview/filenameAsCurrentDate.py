import datetime

def fileNameAsDate():

    filename = datetime.datetime.now()

    with open(filename.strftime("%d %B %Y")+".txt","w") as f:
        f.write("")

fileNameAsDate()