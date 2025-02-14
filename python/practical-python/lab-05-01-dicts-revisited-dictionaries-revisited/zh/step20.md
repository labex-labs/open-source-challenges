# 练习 5.3：类的作用

构成类定义的内容由该类的所有实例共享。注意，所有实例都有一个指向其关联类的链接：

```python
>>> goog.__class__
... 查看输出...
>>> ibm.__class__
... 查看输出...
>>>
```

尝试在实例上调用一个方法：

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

注意，名称 `cost` 既不在 `goog.__dict__` 中定义，也不在 `ibm.__dict__` 中定义。相反，它是由类字典提供的。试试这个：

```python
>>> Stock.__dict__['cost']
... 查看输出...
>>>
```

尝试通过字典直接调用 `cost()` 方法：

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

注意你是如何调用类定义中定义的函数的，以及 `self` 参数是如何获取实例的。

尝试向 `Stock` 类添加一个新属性：

```python
>>> Stock.foo = 42
>>>
```

注意这个新属性现在如何在所有实例上显示：

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

然而，注意它并不是实例字典的一部分：

```python
>>> goog.__dict__
... 查看输出并注意没有 'foo' 属性...
>>>
```

你可以在实例上访问 `foo` 属性的原因是，如果 Python 在实例本身找不到某个东西，它总是会检查类字典。

注意：本练习的这部分说明了所谓的类变量。例如，假设你有这样一个类：

```python
class Foo(object):
     a = 13                  # 类变量
     def __init__(self,b):
         self.b = b          # 实例变量
```

在这个类中，在类本身的主体中赋值的变量 `a` 是一个“类变量”。它由所有创建的实例共享。例如：

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # 检查类变量（两个实例相同）
13
>>> g.a
13
>>> f.b          # 检查实例变量（不同）
10
>>> g.b
20
>>> Foo.a = 42   # 更改类变量的值
>>> f.a
42
>>> g.a
42
>>>
```
