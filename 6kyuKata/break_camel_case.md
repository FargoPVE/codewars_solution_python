# CodeWars Solutions [Python]
___
__Break camelCase__
### DESCRIPTION:

Complete the solution so that the function will break up camel casing, using a space between words.



### Examples ###
```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```
___
#### Solution

```Python
def solution(s):
    test_list_for_iteration = []
    for enum in s:
        if enum.isupper():
            test_list_for_iteration.append(' ')
            test_list_for_iteration.append(enum)
        else:
            test_list_for_iteration.append(enum)
    return ''.join(test_list_for_iteration)
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5208f99aee097e6552000148)
