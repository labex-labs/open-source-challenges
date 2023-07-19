#!/bin/zsh
(((cd /home/labex/project/git-playground && cat ~/.zsh_history | grep -v grep | grep "git rev-parse") && (cd /home/labex/project/git-playground && cat ~/.zsh_history | grep -v grep | grep "abbrev-ref"))
|| ((cd /home/labex/project/git-playground && cat ~/.zsh_history | grep -v grep | grep "git branch") && (cd /home/labex/project/git-playground && cat ~/.zsh_history | grep -v grep | grep "show-current"))
|| ((cd /home/labex/project/git-playground && cat ~/.zsh_history | grep -v grep | grep "git symbolic-ref") && (cd /home/labex/project/git-playground && cat ~/.zsh_history | grep -v grep | grep "short"))
) && echo "True"
