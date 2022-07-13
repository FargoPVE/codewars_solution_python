# CodeWars Solutions [Python]
___
__Grasshopper - Personalized Message__
### DESCRIPTION:
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

| case              |    return     |
|-------------------|:-------------:|
| name equals owner | 	'Hello boss' |
| otherwise         | 'Hello guest' |
___
#### Solution

```Python
def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'
```
___
[See on CodeWars.com](https://www.codewars.com/kata/5772da22b89313a4d50012f7)
