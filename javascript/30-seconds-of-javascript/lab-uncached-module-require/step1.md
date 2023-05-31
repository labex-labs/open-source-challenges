# Uncached Module Require

> To start practicing coding, open the Terminal/SSH and type `node`.

Loads a module after removing it from the cache (if exists).

- Use `delete` to remove the module from the cache (if exists).
- Use `require()` to load the module again.

```js
const requireUncached = module => {
  delete require.cache[require.resolve(module)];
  return require(module);
};
```

```js
const fs = requireUncached('fs'); // 'fs' will be loaded fresh every time
```
