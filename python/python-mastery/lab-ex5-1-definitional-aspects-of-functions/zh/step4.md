# 设计挑战：CSV 表头

代码假设 CSV 数据的第一行总是包含列名。然而，情况并非总是如此。例如，文件`portfolio_noheader.csv`包含数据，但没有列名。

你将如何重构代码以适应缺少的列名，改为由调用者手动提供这些列名呢？
