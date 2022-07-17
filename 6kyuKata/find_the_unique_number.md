# CodeWars Solutions [Python]
___
__Find the unique number__
### DESCRIPTION:

There is an array with some numbers. All numbers are equal except for one. Try to find it!

```
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)\
[Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)\
[Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)

___
#### Solution

```Python
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
```
#### Solution 2

```Python
def find_uniq(arr):
    arr.sort()
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]
    return n
```
___
[See on CodeWars.com](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
