#!/bin/usr/env bash
file="$1"

while read -r line
do
    git clone "$line"

done < "$1"
