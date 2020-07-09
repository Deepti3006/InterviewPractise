def arrangeArrayAlternatively(arr):

    new_arr =[]
    max_value=0
    min_value=0
    size_arr = len(arr)
    while size_arr > 0:
        max_value=max(arr)
        min_value=min(arr)
        if max_value not in new_arr:
            new_arr.append(max_value)
        if min_value not in new_arr:
            new_arr.append(min_value)
        arr.remove(min_value)
        if max_value in arr:
            arr.remove(max_value)
        if min_value in arr:
            arr.remove(min_value)
        size_arr = size_arr -2
    print(new_arr)
arr=[10,20,30,40,50,60,70,80,90,100,110]
arrangeArrayAlternatively(arr)