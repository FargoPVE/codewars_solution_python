# CodeWars Solutions [Python]
___
__Shortest Word__
### DESCRIPTION:

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
___
#### Solution

```Python
def find_short(s):
    return min(map(len, [i for i in s.split()]))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9)
