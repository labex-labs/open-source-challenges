#!/bin/zsh
grep -q "def" ~/.python_history && grep -q ":" ~/.python_history && echo "True"
