#!/bin/zsh
# Running the program confirms that the file is closed
# after being written.
cd /home/labex/project
go run defer.go | grep "creating"