# 通过继承（Inheritance）读取属性（Attribute）

从逻辑上讲，查找属性的过程如下。首先，检查本地的 `__dict__`。如果未找到，则查找类的 `__dict__`。如果在类中也未找到，则通过 `__bases__` 查找基类（Base Class）。不过，接下来会讨论其中一些微妙的方面。
