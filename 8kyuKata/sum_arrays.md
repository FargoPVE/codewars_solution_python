# CodeWars Solutions [Python]
___
__Sum Arrays__
### DESCRIPTION:
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

##### Examples
Input: [1, 5.2, 4, 0, -1]\
__Output: 9.2__

Input: []\
__Output: 0__

Input: [-2.398]\
__Output: -2.398__

##### Assumptions
* You can assume that you are only given numbers.
* You cannot assume the size of the array.
* You can assume that you do get an array and if the array is empty, return 0.
### What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.\
Advanced users may find this extremely easy and can easily write this in one line.
___
#### Solution

```Python
def sum_array(a):
    if len(a) <= 0:
        return 0
    else:
        return sum(a[i] for i in range(0, len(a)))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/53dc54212259ed3d4f00071c/python)
