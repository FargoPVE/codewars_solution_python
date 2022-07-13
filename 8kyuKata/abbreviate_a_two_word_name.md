# CodeWars Solutions [Python]
___
__Abbreviate a Two Word Name__
### DESCRIPTION:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

`Sam Harris => S.H`

`patrick feeney => P.F`
___
#### Solution

```Python
def abbrev_name(name):
    return '.'.join([i[0] for i in name.split(' ')]).title()
```
___
[See on CodeWars.com](https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3)
