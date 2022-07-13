# CodeWars Solutions [Python]
___
__Beginner - Reduce but Grow__
### DESCRIPTION:
Given a non-empty array of integers, return the result of multiplying the values together in order. 

### Example:

```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```
___
#### Solution

```Python
from functools import reduce


def grow(arr):
    return reduce(lambda x,y: x*y, arr)
```
___
[See on CodeWars.com](https://www.codewars.com/kata/57f780909f7e8e3183000078)
