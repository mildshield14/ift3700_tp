#!/bin/bash

# Find all empty directories and subdirectories
for d in $(find . -type d)
do
    # If directory is empty
    if [ -z "$(ls -A $d)" ]
    then
        # Add 1.1 cleaned.csv file
        touch "$d/.gitkeep"
    fi
done