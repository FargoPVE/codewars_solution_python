# CodeWars Solutions [Python]

___
__Disemvowel Trolls__

### DESCRIPTION:

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the
threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
___

#### Solution

```Python
def disemvowel(string_):
    return ''.join(map(str, [l for l in string_ if l.lower() not in ('a', 'e', 'i', 'o', 'u')]))
```

___
[See on CodeWars.com](https://www.codewars.com/kata/52fba66badcd10859f00097e)
