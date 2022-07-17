# CodeWars Solutions [Python]
___
__Descending Order__
### DESCRIPTION:

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 

Essentially, rearrange the digits to create the highest possible number.

### Examples: ###
Input: `42145` Output: `54421`

Input: `145263` Output: `654321`

Input: `123456789` Output: `987654321`
___
#### Solution

```Python
def descending_order(num):
    out_list = [int(i) for i in str(num)]
    out_list.sort(reverse=True)
    return int(''.join((str(i) for i in out_list)))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5467e4d82edf8bbf40000155)
