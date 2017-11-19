

def merge(left, right, result):
    swaps = 0
    result = []
    i, j = 0, 0
    while (len(left) > i and len(right) > j):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            swaps += len(left) - i
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result, swaps


def mergesort(lists, result):
    if len(lists) < 2:
        return lists, 0
    else:
        middle = int(len(lists) // 2)
        left, swaps0 = mergesort(lists[:middle], result[:middle])
        right, swaps1 = mergesort(lists[middle:], result[middle:])
        res, swaps = merge(left, right, result)
        return res, (swaps + swaps0 + swaps1)


def countInversions(arr):
    # Complete this function
    result = []
    sort_arr, swaps = mergesort(arr, result)
    return swaps
