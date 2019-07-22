#!/bin/bash
# Basic while loop
counter=1
while [ $counter -le 31 ]
do
    echo $counter
    ((counter++))
done
echo All done