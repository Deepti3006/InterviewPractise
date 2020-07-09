def typeErrorExceptionHandling():

    try:
        a = 10
        print(a+ "dont worjk")
    except TypeError:
        print("Hitting type error exception as we are having function which cannot be used.")

typeErrorExceptionHandling()