#!/bin/zsh
cd ~/project/mysite
python manage.py test polls | grep "10"
