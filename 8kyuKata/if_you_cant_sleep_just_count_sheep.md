# CodeWars Solutions [Python]
___
__If you can't sleep, just count sheep!!__
### DESCRIPTION:
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: `"1 sheep...2 sheep...3 sheep..."`. Input will always be valid, i.e. no negative integers.


___
#### Solution

```Python
def count_sheep(n):
    return ''.join([f'{i} sheep...' for i in range(1, n+1)])
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5b077ebdaf15be5c7f000077)
