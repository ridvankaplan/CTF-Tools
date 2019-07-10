# Rıdvan KAPLAN
# The script for challenge on HackTheBox
# Challenge name is Emdee five for life
# The link : https://www.hackthebox.eu/home/challenges/Web
# Challenge : Post request the string md5 hashing in a session


#!/usr/bin/python3
import requests
import re
import hashlib


def request():
	# Target url : http://docker.hackthebox.eu:42765/
	# Regex : egrep '[a-zA-Z0-9]{20}'
	url = 'http://docker.hackthebox.eu:42849/'
	session = requests.session()
	html = (session.get(url)).text
	data = re.findall(r'[a-zA-Z0-9]{20}', str(html)) # String in page
	md5 = (hashlib.md5(data[0].encode())).hexdigest()
	requestPost(md5, url ,session)


def requestPost(md5, url, session):
	post = {'hash': md5}
	send = session.post(url=url,data=post)
	print(send.text)


def main():
	request()

main()
