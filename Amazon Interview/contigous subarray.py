def contigousSubArray(arr,s):

   arr_elme = arr[0]
   max_arr = arr[0]

   for i in range(len(arr)):
       for y in range(i+1,len(arr)):
           for z in range(y+1,len(arr)):
               if arr[i] +arr[y] +arr[z] == s:
                   print(arr[i],arr[y],arr[z])



arr =[1,2,3,7,5,8,6]
s= 12

contigousSubArray(arr,s)