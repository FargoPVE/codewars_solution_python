# CodeWars Solutions [Python]
___
__Odd or Even?__
### DESCRIPTION:

#### Task:
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching `"odd"` or `"even"`.

If the input array is empty consider it as: `[0]` (array with a zero).



### Examples: ###
```angular2html
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
```
Have fun!
___
#### Solution

```Python
def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
```

#### Solution 2

```Python
def odd_or_even(arr):
    if len(arr):
        if sum(arr) % 2 == 0:
            return "even"
        else:
            return 'odd'
    else:
        return 'even'
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5949481f86420f59480000e7)
