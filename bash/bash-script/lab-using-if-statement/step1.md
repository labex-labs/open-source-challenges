# Using if statement

## Problem

Create a Bash script that checks if a number is one digit or two digits. The script should take a number as input and output "It is a one digit number" if the number is less than 10, and "It is a two digit number" if the number is greater than or equal to 10. 

## Requirements

- The script should be named `simple_if.sh`.
- The script should use if statement to check the number.
- The script should take a number as input.
- The script should output "It is a one digit number" if the number is less than 10.
- The script should output "It is a two digit number" if the number is greater than or equal to 10.

## Solution

```bash
#!/bin/bash
read -p "Enter a number: " n
if [ $n -lt 10 ];
then
    echo "It is a one digit number"
else
    echo "It is a two digit number"
fi
```

Save the above script in a file named `simple_if.sh`. Run the script with the following command:

```bash
bash simple_if.sh
```

