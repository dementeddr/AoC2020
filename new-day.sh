#!/usr/bin/zsh

NDIR=$1"day"

mkdir $NDIR

cp template.py "$NDIR/$1-1.py"

touch "$NDIR/input-d$1.txt"
