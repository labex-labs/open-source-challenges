#!/bin/zsh
# Running this program shows the first operation timing
# out and the second succeeding.
cd /home/labex/project
go run timeouts.go | grep "timeout 1"