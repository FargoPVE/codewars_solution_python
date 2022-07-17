# CodeWars Solutions [Python]
___
__Square Every Digit__
### DESCRIPTION:

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 8^1 and 1^2 is 1.

__Note__: The function accepts an integer and returns an integer

___
#### Solution

```Python
def square_digits(num):
    return int(''.join(map(str, [int(i) ** 2 for i in str(num)])))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/546e2562b03326a88e000020)
