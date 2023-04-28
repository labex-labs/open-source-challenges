---
title: Change the last commit's author
---

Updates the last commit's author without changing its contents.

- Use `git commit --amend` to edit the last commit.
- Use the `--author` option to change the `<name>` and `<email>` of the commit's author.

```shell
git commit --amend --author="<name> <email>"
```

```shell
# Make some changes to files
git add .
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
# The last commit's author is now `Duck Quackers`
```
