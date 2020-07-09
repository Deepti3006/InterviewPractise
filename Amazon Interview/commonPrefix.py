def commonPrefix(arr):

    s1= set(arr[0])
    s2 = set(arr[2])
    s3 = set(arr[1])
    string1 =""
    for i in range(len(arr)):
        for y in range(len(arr)):
            for z in range(len(arr)):
                if arr[i][i] == arr[y][i] == arr[z][i]:
                    if arr[i][i] not in string1:
                        string1 = string1+arr[i][i]

    print(string1)


    #print(sorted(s1.intersection(s2,s3)))
    #print("".join(sorted(s1.intersection(s2,s3))))








arr = ["flower", "flow", "flight","flee","fipi"]
commonPrefix(arr)

