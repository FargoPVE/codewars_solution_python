# CodeWars Solutions [Python]
___
__Sum of the first nth term of Series__
### DESCRIPTION:

### Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).

```
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
```
### Rules:
* You need to round the answer to 2 decimal places and return it as String.

* If the given value is 0 then it should return 0.00

* You will only be given Natural Numbers as arguments.

### Examples: ###
```angular2html
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
```
___
#### Solution

```Python
def series_sum(n):
    if n == 0:
        return ("%.2f" % 0)
    else:
        n = n - 1
        sum_list = [1]
        while n > 0:
            x = 1 / float(n * 3 + 1)
            sum_list.append(x)
            n = n - 1
        return ("%.2f" % sum(sum_list))

```
___
[See on CodeWars.com](https://www.codewars.com/kata/555eded1ad94b00403000071)
