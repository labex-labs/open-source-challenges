# Argument Coalescing

> To start practicing coding, open the Terminal/SSH and type `node`.

Returns the first defined, non-null argument.

- Use `Array.prototype.find()` and `Array.prototype.includes()` to find the first value that is not equal to `undefined` or `null`.

```js
const coalesce = (...args) => args.find(v => ![undefined, null].includes(v));
```

```js
coalesce(null, undefined, '', NaN, 'Waldo'); // ''
```
