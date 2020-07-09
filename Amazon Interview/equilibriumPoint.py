def equilibriumPoint(arr):

   right_sum =0
   left_sum = 0
   total = sum(arr)

   for i in range(len(arr)):
       right_sum = total - left_sum - arr[i]
       if right_sum == left_sum:
            print(i)
            print(arr[i])
       left_sum = left_sum+arr[i]

arr=[1,3,5,2,2]
equilibriumPoint(arr)
