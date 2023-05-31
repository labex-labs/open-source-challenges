# String to Slug

> To start practicing coding, open the Terminal/SSH and type `node`.

Converts a string to a URL-friendly slug.

- Use `String.prototype.toLowerCase()` and `String.prototype.trim()` to normalize the string.
- Use `String.prototype.replace()` to replace spaces, dashes and underscores with `-` and remove special characters.

```js
const slugify = str =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
```

```js
slugify('Hello World!'); // 'hello-world'
```
