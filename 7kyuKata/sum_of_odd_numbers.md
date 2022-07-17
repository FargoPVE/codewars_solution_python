# CodeWars Solutions [Python]
___
__Sum of odd numbers__
### DESCRIPTION:

Given the triangle of consecutive odd numbers:

```angular2html
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (`Input --> Output`)

```
1 -->  1
2 --> 3 + 5 = 8
```
___
#### Solution

```Python
def row_sum_odd_numbers(n):
    return n ** 3
```
___
[See on CodeWars.com](https://www.codewars.com/kata/55fd2d567d94ac3bc9000064)
