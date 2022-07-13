def merge_arrays(arr1, arr2):
    return sorted(list(map(int, set(arr1+arr2))))