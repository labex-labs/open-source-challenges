# 生命周期

生命周期是编译器（更具体地说是其借用检查器）用于确保所有借用有效的一种结构。具体来说，变量的生命周期从创建时开始，到销毁时结束。虽然生命周期和作用域经常一起被提及，但它们并不相同。

例如，当我们通过 `&` 借用一个变量时，借用的生命周期由其声明位置决定。因此，只要借用在出借者被销毁之前结束，它就是有效的。然而，借用的作用域由引用的使用位置决定。

在下面的示例以及本节的其余部分中，我们将看到生命周期与作用域的关系，以及两者的区别。

```rust
// 下面用线条标注了每个变量的创建和销毁，以此表示生命周期。
// `i` 的生命周期最长，因为它的作用域完全包含了 `borrow1` 和 `borrow2`。
// 由于 `borrow1` 和 `borrow2` 不相交，所以它们的持续时间比较无关紧要。
fn main() {
    let i = 3; // `i` 的生命周期开始。 ────────────────┐
    //                                                     │
    { //                                                   │
        let borrow1 = &i; // `borrow1` 的生命周期开始。 ──┐│
        //                                                ││
        println!("borrow1: {}", borrow1); //              ││
    } // `borrow1` 结束。 ─────────────────────────────────┘│
    //                                                     │
    //                                                     │
    { //                                                   │
        let borrow2 = &i; // `borrow2` 的生命周期开始。 ──┐│
        //                                                ││
        println!("borrow2: {}", borrow2); //              ││
    } // `borrow2` 结束。 ─────────────────────────────────┘│
    //                                                     │
}   // 生命周期结束。 ─────────────────────────────────────┘
```

请注意，没有为生命周期标签分配名称或类型。正如我们将看到的，这限制了生命周期的使用方式。
