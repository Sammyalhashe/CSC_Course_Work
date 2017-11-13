## given an array of ints, find an element in question. If there return True
## If not there, return false

def binarySearch(array,search_int):

    ## Sort the array
    Quick_Sort(array)

    ## Iterative approach to binary search on the array

    left = 0
    right = len(array) - 1

    while(left<=right):
        mid = int(left+((right-left)/2)) #middle of hte array

        if(array[mid] == search_int):
            return True
        elif(search_int < array[mid]):
            right = mid - 1
        else:
            leftleft = mid + 1