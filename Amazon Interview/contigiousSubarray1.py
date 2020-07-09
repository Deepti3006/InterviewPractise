import itertools
from array import array
import numpy as np
def contigiousSubarray1(arr):

    arr_sum =[]
    arr_sum_1 =[]
    arr_check =[]
    sum1 =0
    for i in range(1,len(arr)):
        seq = itertools.combinations(arr,i)
        lst = list(seq)
        arr_sum_1 = np.array(lst)
        arr_sum.append(arr_sum_1)
        print(arr_sum)
    for i in arr_sum:
        sum1 = sum(i)
        arr_check.append(sum1)
        print(sum1)







arr = [-2,1,-3,4,-1,2,1,-5,4]


contigiousSubarray1(arr)