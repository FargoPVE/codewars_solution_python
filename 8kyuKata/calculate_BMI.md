# CodeWars Solutions [Python]
___
__Calculate BMI__
### DESCRIPTION:
Write function bmi that calculates body mass index `(bmi = weight / height2)`.

* if bmi <= 18.5 return "Underweight"

* if bmi <= 25.0 return "Normal"

* if bmi <= 30.0 return "Overweight"

* if bmi > 30 return "Obese"
___
#### Solution

```Python
def bmi(weight, height):
    b = weight / (height ** 2)
    if b <= 18.5:
        return "Underweight"
    elif 18.5 < b <= 25.0:
        return "Normal"
    elif 25.0 < b <= 30.0:
        return "Overweight"
    else:
        return "Obese"
```
___
[See on CodeWars.com](https://www.codewars.com/kata/57a429e253ba3381850000fb)
