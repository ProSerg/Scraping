#!/usr/bin/env python3


# working with network
import urllib.request
# parsing HTML
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def main():
	print("Hello,World!{}",get_html("http://yandex.ru"))
	pass
	
if  __name__ == "__main__":
	main()
	


