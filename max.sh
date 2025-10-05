#!/bin/bash

echo "enter a number"
read "number1"

echo "enter another number"
read "number2"

if [ "$number1" -gt "$number2" ]; then
    echo "$number1" is the larger number
else
    echo "$number2" is the larger number
fi


