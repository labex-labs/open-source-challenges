#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep 'git rm --cached "file1.txt"') && (cat ~/.zsh_history | grep -v grep | grep "git commit --amend") && (cd /home/labex/project/git-playground && git log | grep "add git-playground.txt") && echo "True"

