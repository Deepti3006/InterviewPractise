class missinNumberInArray():
    def findmissing(self):
        a = {1,2,4,5,7,9}
        original_list = {1,2,3,4,5,6,7,8,9,10}
        result = original_list.symmetric_difference(a)
        print(result)
        print("I am trhough")

mN = missinNumberInArray()
mN.findmissing()

