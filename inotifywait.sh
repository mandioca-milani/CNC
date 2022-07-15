#!/bin/bash

inotifywait --quiet --monitor --fromfile ./inotifywait.txt | while read DIRECTORY EVENT FILE; do
#     echo "$DIRECTORY $FILE $EVENT"

    case $EVENT in
        CLOSE_WRITE,CLOSE)
            FreeCAD --single-instance $DIRECTORY$FILE &
            ;;
    esac
done
