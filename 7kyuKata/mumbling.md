# CodeWars Solutions [Python]
___
__Mumbling__
### DESCRIPTION:

This time no story, no theory. The examples below show you how to write function `accum`:

### Examples: ###
```angular2html
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```
The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.
___
#### Solution

```Python
def accum(s):
    result_list = []
    for j, i in enumerate(s):
        if i.islower() == True:
            result_list.append(i.upper() + i * j)
        else:
            result_list.append(i + (i.lower() * j))
    return '-'.join(result_list)

```
___
[See on CodeWars.com](https://www.codewars.com/kata/5667e8f4e3f572a8f2000039)
