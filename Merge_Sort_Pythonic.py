# More pythonic implementation of merge sort

def Merge_Sort_Pythonic(array):
    temp = [0 for i in range(len(array))]
    mergesort_Pythonic(array,temp)

def mergesort_Pythonic(array,temp):
    if(leftStart>=rightEnd):
        return
    mid = int((len(array))/2)
    leftStart = 0
    rightEnd  = len(array)-1
    mergesort_Pythonic(array[:mid],temp[:mid])
    mergesort_Pythonic(array[mid:],temp[mid:])
    merge(array,temp,leftStart,rightEnd)

def merge(array,temp,left,right):
    leftEnd = int((left+right)/2)
    rightStart = leftEnd + 1
    #size = right - left + 1 #len(temp)?

    left_ind = leftStart
    right_ind = rightStart
    index = leftStart

    while(left_ind<=leftEnd and right_ind<=rightEnd):
        if(array[left_ind]<array[right_ind]):
            temp[index] = array[left_ind]
            left_ind+=1
        else:
            temp[index] = array[right_ind]
            right_ind+=1
        index+=1

    ## Once one of either left_ind or right_ind goes out of bounds, we have to copy into temp the rest of
    # the elements
    # Note: inly one of these loops will execute as one of right_ind or left_ind will have already reached
    # it's boundary value

    for i in range(left_ind,leftEnd):
        temp[index] = array[i]
        index+=1
    for j in range(right_ind,rightEnd):
        temp[index] = array[j]
        index+=1

    ## Copy over the contents of temp back into array:

    for m in range(len(array)):
        array[m] = temp[m]
