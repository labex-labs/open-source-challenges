# A Sample Program

Let's solve the following problem:

> One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. Each day thereafter, you go out double the number of bills. How long does it take for the stack of bills to exceed the height of the tower?

Here's a solution:

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

When you run it, you get the following output:

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Number of days 23
Number of bills 4194304
Final height 461.37344
```

Using this program as a guide, you can learn a number of important core concepts about Python.
