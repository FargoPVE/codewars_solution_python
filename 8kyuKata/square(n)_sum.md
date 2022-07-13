# CodeWars Solutions [Python]
___
__Square(n) Sum__
### DESCRIPTION:
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for `[1, 2, 2]` it should return `9` because `1^2 + 2^2 + 2^2 = 9`.
___
#### Solution

```Python
def square_sum(numbers):
    return sum([i**2 for i in numbers])
```
___
[See on CodeWars.com](https://www.codewars.com/kata/515e271a311df0350d00000f)
