# Pulling All Submodules from Remote

You have a Git repository with submodules that need to be updated from their respective remotes. Manually pulling each submodule can be time-consuming and error-prone. You need a way to pull all submodules at once.

Assuming you have a Git repository named `git` that contains submodules, you can pull all submodules from their respective remotes using the following command:
```shell
cd git
git submodule update --recursive --remote
```

This command updates all submodules in the repository to the latest version available in their respective remotes.
