#!/bin/zsh
(cd /home/labex/project/git-playground && ! git stash list | grep "stash@") && echo "True"
