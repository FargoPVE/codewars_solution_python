# CodeWars Solutions [Python]
___
__Invert values__
### DESCRIPTION:
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```
You can assume that all values are integers. Do not mutate the input array/list.
___
#### Solution #1

```Python
def invert(lst):
    return [-val for val in lst]
```
___
#### Solution #2

```Python
def invert_2(lst):
    output_list = []
    for char in lst:
        if char < 0:
            output_list.append(abs(char))
        else:
            output_list.append(-char)
    return output_list
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad)
