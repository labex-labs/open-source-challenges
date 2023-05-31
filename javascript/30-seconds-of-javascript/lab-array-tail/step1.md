# Array Tail

> To start practicing coding, open the Terminal/SSH and type `node`.

Returns all elements in an array except for the first one.

- Use `Array.prototype.slice()`to return the array without the first element if `Array.prototype.length` is more than `1`.
- Otherwise, return the whole array.

```js
const tail = arr => (arr.length > 1 ? arr.slice(1) : arr);
```

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
