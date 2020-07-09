class Error(Exception):
    pass

class ValueTooSmall(Error):
    pass

class ValueTooBig(Error):
    pass

a =10

try:
    b= int(input("Enter the number"))
    if b>a:
        raise ValueTooSmall
    elif b<a:
        raise ValueTooBig
    else:
        print("No exception good")
except ValueTooSmall:
    print("Value is too small")

except ValueTooBig:
    print("Value is too big")

finally:
    print(a)




