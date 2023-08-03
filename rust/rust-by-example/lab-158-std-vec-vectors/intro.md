# Introduction

In this lab, we will be learning about vectors, which are re-sizable arrays in Rust that can grow or shrink at any time. A vector is represented using three parameters: a pointer to the data, length, and capacity. The capacity indicates how much memory is reserved for the vector, and when the length surpasses the capacity, the vector is reallocated with a larger capacity. We can collect iterators into vectors using the `collect` method, initialize vectors using the `vec!` macro, insert new elements at the end using the `push` method, and get the number of elements using the `len` method. We can also access elements using indexing, remove the last element using the `pop` method, and iterate over the vector using the `iter` or `iter_mut` methods. Additionally, there are more methods available for vectors in the `std::vec` module.

> **Note:** If the lab does not specify a file name, you can use any file name you want. For example, you can use `main.rs`, compile and run it with `rustc main.rs && ./main`.