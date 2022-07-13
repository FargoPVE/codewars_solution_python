# CodeWars Solutions [Python]
___
__Reversed sequence__
### DESCRIPTION:
Build a function that returns an array of integers from n to `1` where `n>0`.

Example : `n=5` --> `[5,4,3,2,1]`
___
#### Solution

```Python
def reverse_seq(n):
    return [num for num in range(n, 0, -1)]
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5a00e05cc374cb34d100000d)
