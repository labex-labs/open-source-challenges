# 简介

在本实验中，我们学习了 Rust 中的格式化以及如何使用 `format!` 宏来格式化变量。我们了解到格式化是通过格式字符串指定的，并且可以使用不同的参数类型以不同的方式格式化同一个变量。最常见的格式化特性是 `Display`，它处理参数类型未指定的情况。我们看到了一个为 `City` 结构体实现 `Display` 特性的示例，在该示例中我们格式化了纬度和经度值。我们还看到了一个 `Color` 结构体的示例，并被要求为其实现 `Display` 特性以显示 RGB 值及其十六进制表示形式。

> **注意**：如果实验未指定文件名，你可以使用任何你想要的文件名。例如，你可以使用 `main.rs`，并通过 `rustc main.rs &&./main` 进行编译和运行。
