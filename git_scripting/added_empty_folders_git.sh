#!/bin/bash

# Find all empty directories and subdirectories
for d in $(find . -type d)
do
    # If directory is empty
    if [ -z "$(ls -A $d)" ]
    then
        # Add .gitkeep file
        touch "$d/.gitkeep"
    fi
done