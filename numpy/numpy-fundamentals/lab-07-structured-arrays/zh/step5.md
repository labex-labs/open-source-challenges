# 比较结构化数组

如果两个结构化数组的数据类型相同，我们可以使用相等运算符（`==`）对它们进行比较。这将返回一个布尔数组，指示哪些元素在所有字段中具有相同的值。

```python
# 比较两个结构化数组
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
