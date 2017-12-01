# More pythonic implementation of merge sort


def Merge_Sort_Pythonic(array):
    return mergesort_Pythonic(array)


def mergesort_Pythonic(array):
    if(len(array) < 2):
        return array
    # Integer division for middle index
    mid = ((len(array)) // 2)

    # Merge-sort left and right halves
    left = mergesort_Pythonic(array[:mid])
    right = mergesort_Pythonic(array[mid:])
    res = merge(left, right)
    return res


def merge(left, right):
    # size = right - left + 1 #len(temp)?
    i, j, ind = 0, 0, 0
    l, r = len(left), len(right)
    length = l + r
    temp = [0 for i in range(length)]

    while(len(left) > i and len(right) > j):
        if(left[i] < right[j]):
            temp[ind] = left[i]
            i += 1
        else:
            temp[ind] = right[j]
            j += 1

        ind += 1

    # Once one of either left_ind or right_ind goes out of bounds, we have to copy into temp the rest of
    # the elements
    # Note: inly one of these loops will execute as one of right_ind or left_ind will have already reached
    # it's boundary value
        if i == len(left) or j == len(right):
            temp.extend(left[i:] or right[j:])
            break

    return temp


if __name__ == '__main__':
    test = [1, 32, 122, 32, 12, 311, 2, 3, 21, 2]
    result = Merge_Sort_Pythonic(test)
    print(result)
