# 使用多个字段进行索引

我们可以通过传递字段名列表来对结构化数组进行多个字段的索引。这将返回一个只包含指定字段的新结构化数组。

```python
# 使用多个字段进行索引
subset = x[['name', 'age']]
```
