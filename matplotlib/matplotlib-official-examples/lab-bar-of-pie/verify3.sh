#!/bin/zsh

cd ~/project
git diff | grep 'subplots'
git diff | grep -E 'pie.*\('
