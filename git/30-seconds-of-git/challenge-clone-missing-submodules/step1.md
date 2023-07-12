# Clone Missing Submodules

## Problem

You are working on a project that contains submodules. When you clone the project, the submodules are not automatically cloned. This causes issues when trying to build or run the project. You need to clone the missing submodules and checkout the correct commits.

## Example

For this challenge, we will use the Git repository named `https://github.com/git/git`. This repository contains submodules that are not automatically cloned when you clone the repository.

To clone the missing submodules and checkout the correct commits, follow these steps:

1. Change into the repository directory.
2. Initialize the submodules.
3. Checkout to the correct commit of the submodule, i.e. the `master` branch.

Here's the final result:
```shell
Submodule 'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path 'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path 'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```

