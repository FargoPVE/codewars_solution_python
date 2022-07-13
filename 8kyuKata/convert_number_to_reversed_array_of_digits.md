# CodeWars Solutions [Python]
___
__Convert number to reversed array of digits__
### DESCRIPTION:
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

### Example(Input => Output):
```
348597 => [7,9,5,8,4,3]
0 => [0]
```
___
#### Solution

```Python
def digitize(n):
    return list(reversed([int(i) for i in str(n)]))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5583090cbe83f4fd8c000051)
