#!/bin/zsh
((cat ~/.zsh_history | grep -v grep | grep "git config --global -e") || (cat ~/.zsh_history | grep -v grep | grep "git configuration --global -e")) && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"
