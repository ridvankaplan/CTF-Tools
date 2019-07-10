# Rıdvan KAPLAN
# The script for challenge on HackTheBox
# Challenge name is Eternal Loop
# The link : https://www.hackthebox.eu/home/challenges/Misc
# Challenge : Password of zip file is a name of next zip file and in eternal loop


#!/bin/bash

for i in {1..500}
	do
		name=$(ls CTF/)
		zip_output=$(unzip -Z1 CTF/$name)
		password=$(echo $zip_output | tr --delete .zip)
#		echo $password
		unzip -P $password CTF/$name -d CTF/
		delete=$(rm CTF/$name)
#		echo $i #for control
done
echo "Finished"


