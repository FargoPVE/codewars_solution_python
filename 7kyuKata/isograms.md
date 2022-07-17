# CodeWars Solutions [Python]
___
__Isograms__
### DESCRIPTION:

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

### Examples: ###
```angular2html
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
```
___
#### Solution

```Python
def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)
```
___
[See on CodeWars.com](https://www.codewars.com/kata/54ba84be607a92aa900000f1)
