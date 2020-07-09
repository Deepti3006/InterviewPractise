# Built in Exception

def checkAssertionExceoption(a,b):

    try:
        assert(a+b <5)

    except AssertionError:
        print("Hitting exception")

checkAssertionExceoption(1,7)