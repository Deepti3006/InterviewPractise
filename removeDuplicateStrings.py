def removeDuplicateString():

    a = input("Enter the string")

    for char in a:
        if a.count(char) > 1:
            print("I am in")
            b= a.replace(char,'')
    print(b)
#removeDuplicateString()

def setsort():
    arr ={'G4','G3','R1','R4','G2','G5','R2','G1','R3','R5'}
    sorted_arr = sorted(arr)
    print(sorted_arr)
    arr_need =sorted_arr[::-1]
    print(arr_need)


#setsort()

def sort_setsort():
    arr = {'G4', 'G3', 'R1', 'R4', 'G2', 'G5', 'R2', 'G1', 'R3', 'R5'}
    new_arr_R = []
    new_arr_G =[]
    len_arr = len(arr)
    for i in arr:
        if(i=='R1' or i=='R2' or i=='R3' or i=='R4' or i=='R5'):
            new_arr_R.append(i)
        else:
            new_arr_G.append(i)
            print("Not removing")
    arr = sorted(new_arr_R) + sorted(new_arr_G)
    print(new_arr_G)
    print(new_arr_R)
    print(arr)
sort_setsort()

