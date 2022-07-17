def duplicates(arr):
    count = 0
    arr.sort()
    i = 0
    while i < (len(arr) - 1):
        if (arr[i] == arr[i + 1]):
            count += 1
            i = i + 2
        else:
            i += 1
    return count
