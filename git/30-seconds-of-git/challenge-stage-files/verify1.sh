#!/bin/zsh
(cd /home/labex/project/git-playground | git diff --cached | grep "1.py") && (cd /home/labex/project/git-playground | git diff --cached | grep "2.py")&&(cd /home/labex/project/git-playground | git diff --cached | grep "index.html") && (cd /home/labex/project/git-playground | git diff --cached | grep "one.js") && (cd /home/labex/project/git-playground | git diff --cached | grep "style.css") && (cd /home/labex/project/git-playground | git diff --cached | grep "two.js")&&echo "True"

