def  assertionException(a,b):

    try:
        assert(a+b <5)
    except AssertionError:
        print("a,b isnot working as expected")

def keyException():
    try :
        names ={"1":"Deepti" ,"2":"cisco"}
        names["3"]
    except KeyError:
        print("Key is not seen")

def typeException():
    try :
        a=0
        print(a+"I sm not working")
    except TypeError:
        print("type exception")

assertionException(4,5)
keyException()
typeException()