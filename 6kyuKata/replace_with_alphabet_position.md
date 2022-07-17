# CodeWars Solutions [Python]
___
__Replace With Alphabet Position__
### DESCRIPTION:

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

### Example
```
alphabet_position("The sunset sets at twelve o' clock.")
```
Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )
___
#### Solution

```Python
def alphabet_position(text):
    ord_out_list = []
    for char in list(text.lower()):
        if char.isalpha():
            ord_out_list.append(ord(char) - 96)
        else:
            continue
    return ' '.join(map(str, ord_out_list))
```
___
[See on CodeWars.com](https://www.codewars.com/kata/546f922b54af40e1e90001da)
