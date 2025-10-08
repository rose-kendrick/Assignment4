#!bin/bash

filepath=~dpawlows/Public/Phy380/assignment4/filetest.sh
dir=~/assignment4

cp "$filepath" "$dir"

file=~/assignment4/filetest.sh

if [ -f "$file" ]; then
    permissions=$(ls -l "$file"|awk '{print $1}')
    echo 'permissions: "$permissions"'

    if [ !  -s "$file" ]; then #I had to look up ! -s to get it to ask if the file is not greater than 0 in size. 
	echo 'blank file'

    else
	echo 'file is not blank'
    fi
else
    echo 'the file does not exist'
fi



