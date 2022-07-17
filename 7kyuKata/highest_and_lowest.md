# CodeWars Solutions [Python]
___
__Highest and Lowest__
### DESCRIPTION:

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

### Examples: ###
```python
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
```
### Notes
* All numbers are valid Int32, no need to validate them.
* There will always be at least one number in the input string.
* Output string must be two numbers separated by a single space, and highest number is first.
___
#### Solution

```Python
def high_and_low(numbers):
    return str(max(int(i) for i in numbers.split()))+' '+ str(min(int(i) for i in numbers.split()))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/554b4ac871d6813a03000035)
