def array_left_rotation(a, n, k):
    new_array = [0]*len(a)


    for i in range(len(a)):
        new_array[i-k] = a[i]
    return new_array

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

