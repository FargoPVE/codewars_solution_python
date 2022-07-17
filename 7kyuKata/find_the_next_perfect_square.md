# CodeWars Solutions [Python]
___
__Find the next perfect square!__
### DESCRIPTION:

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the `findNextSquare` method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then `-1` should be returned. You may assume the parameter is non-negative.

### Examples: ###
```angular2html
121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
```
___
#### Solution

```Python
def find_next_square(sq):
    sqr = sq ** 0.5
    if sqr % 1 == 0:
        return (sqr + 1) * (sqr + 1)
    else:
        return -1
```
___
[See on CodeWars.com](https://www.codewars.com/kata/56269eb78ad2e4ced1000013)
