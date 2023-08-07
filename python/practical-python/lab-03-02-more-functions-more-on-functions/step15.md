# Exercise 3.5: Performing Type Conversion

Modify the `parse_csv()` function so that it optionally allows type-conversions to be applied to the returned data. For example:

```python
>>> portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price': 70.44, 'name': 'IBM', 'shares': 100}]

>>> shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
>>> shares_held
[{'name': 'AA', 'shares': 100}, {'name': 'IBM', 'shares': 50}, {'name': 'CAT', 'shares': 150}, {'name': 'MSFT', 'shares': 200}, {'name': 'GE', 'shares': 95}, {'name': 'MSFT', 'shares': 50}, {'name': 'IBM', 'shares': 100}]
>>>
```

You already explored this in [Exercise 2.24](../02_Working_with_data/07_Objects.md). You'll need to insert the following fragment of code into your solution:

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```
