# Hamming Distance

> To start practicing coding, open the Terminal/SSH and type `node`.

Calculates the Hamming distance between two values.

- Use the XOR operator (`^`) to find the bit difference between the two numbers.
- Convert to a binary string using `Number.prototype.toString()`.
- Count and return the number of `1`s in the string, using `String.prototype.match()`.

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || '').length;
```

```js
hammingDistance(2, 3); // 1
```
