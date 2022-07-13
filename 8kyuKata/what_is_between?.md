# CodeWars Solutions [Python]
___
__What is between?__
### DESCRIPTION:
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

```
a = 1
b = 4
--> [1, 2, 3, 4]
```
___
#### Solution

```Python
def between(a, b):
    return list(range(a, b+1))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/55ecd718f46fba02e5000029)
