# CodeWars Solutions [Python]
___
__Convert a string to an array__
### DESCRIPTION:
Write a function to split a string and convert it into an array of words.

### Examples (Input ==> Output):
```
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```
___
#### Solution

```Python
def string_to_array(s):
    return [i for i in s.split()] if s else ['']
```
___
[See on CodeWars.com](https://www.codewars.com/kata/57e76bc428d6fbc2d500036d)
