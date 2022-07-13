# CodeWars Solutions [Python]
___
__Sum of positive__
### DESCRIPTION:
You get an array of numbers, return the sum of all of the positives ones.

Example `[1,-4,7,12]` => `1 + 7 + 12 = 20`

Note: if there is nothing to sum, the sum is default to `0`.
___
#### Solution

```Python
def positive_sum(arr):
    return sum(num for num in arr if num > 0)
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5715eaedb436cf5606000381)
