#!/bin/bash

dasgoclient -query="instance=prod/global dataset=/${2}*/${1}*/NANOAODSIM" > ttt.txt

while read line; do
    echo $line
    if [ $# -gt 2 ]; then
        dasgoclient -query="instance=prod/global summary dataset=${line}"
        echo ""
    fi
done <ttt.txt

rm ttt.txt


