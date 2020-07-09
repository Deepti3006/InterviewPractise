import itertools
def largestNumberFromArray(arr):

   seq = itertools.permutations(arr,len(arr))
   arr_1 = []
   for i in itertools.permutations(arr,len(arr)):
       print(i)
       arr_1.append(i)
   print(len(arr_1))
   print(max(arr_1))
   string1 =str(max(arr_1)).replace(",","")
   s = "".join(string1.split())
   print(s)
arr=[54,546,548,60]
largestNumberFromArray(arr)

