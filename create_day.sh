#!/usr/bin/env bash
ADVENT_HOME="$HOME/AdventOfCode"
if [[ $# -eq 2 ]]
then
    YEAR=$1
    DAY=$2
    NEW_DIR="$ADVENT_HOME/$YEAR/day$DAY"
    echo "Creating files in $NEW_DIR..."
    mkdir -p $NEW_DIR
    sed -e "s;%NEW_DIR%;$NEW_DIR;g" -e "s;%DAY%;$DAY;g" "dayTemplate" > "$NEW_DIR/day$DAY.py"
    touch "$NEW_DIR/day_${DAY}input.txt"
    cd $NEW_DIR
else
    echo "Usage: $0 Year Day"
fi

