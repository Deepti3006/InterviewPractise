def keyExceptionHandling():

    try:
        name = {"1":"deepti","2":"Ananya","3":"Sueu"}
        for key,value in name.items():
            print(name.keys())
        name["Venkata"]

    except KeyError:
        print("I got the print error ")
keyExceptionHandling()

