#!/bin/zsh
(cd /home/labex/project/git-playground && git diff HEAD | grep "1.py") && (cd /home/labex/project/git-playground && git diff HEAD | grep "2.py") && (cd /home/labex/project/git-playground && git diff HEAD | grep "index.html") && (cd /home/labex/project/git-playground && git diff HEAD | grep "one.js") && (cd /home/labex/project/git-playground && git diff HEAD | grep "style.css") && (cd /home/labex/project/git-playground && git diff HEAD | grep "two.js") && echo "True"
