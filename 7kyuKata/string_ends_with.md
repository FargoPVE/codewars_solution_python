# CodeWars Solutions [Python]
___
__String ends with?__
### DESCRIPTION:

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

### Examples: 
``` Python
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```
___
#### Solution

```Python
def solution(string, ending):
    return string.endswith(ending)
```
___
[See on CodeWars.com](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d)
