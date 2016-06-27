#!/usr/bin/env python3


# working with network
import urllib.request
#
import time
import string

# parsing HTML
from bs4 import BeautifulSoup
#
from datetime import datetime
from datetime import date
"""
ПО дате лучше не ориентироваться. Странная система на сайте.
"""

BASE_URL = 'https://www.weblancer.net/jobs/?type=project'

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def get_page_count(html):
	soup = BeautifulSoup( html, "lxml" )
	pag = soup.select("div > ul.navlist > li  > strong > span ")
	return pag[1].text
		
def get_project_count(html):
	soup = BeautifulSoup( html, "lxml" )
	pag = soup.select("div > ul.navlist > li  > strong > span ")
	return pag[1].text
	
def parser(url,count):
	date_today = datetime.now()
	for number in range(1, count + 1) :
		html = get_html(url+"&page={}".format(number))
		soup = BeautifulSoup( html, "lxml" )
		rows = soup.find('div', class_='container-fluid cols_table show_visited' )
		for row in rows:
			print("Title: %s" % row.find('a', class_ = "title" ).text )
			print("Amount: %s" % row.find('div', class_ = "col-sm-2 amount title" ).text.strip() )
			
			date = row.find('span', class_ = "time_ago" )['title']
			date_object = datetime.strptime( date, '%d.%m.%Y в %H:%M')
			date_delta = date_today - date_object
			days = date_delta.days
			hours = date_delta.seconds/3600
			minutes = date_delta.seconds/3600/3600
			if days > 0:
				print("Date: %d dayes" % days )
			else:
				print("Date: %.1f hours" % hours )
	
def main():
	HTML = get_html(BASE_URL)
#	total_pages = get_page_count(HTML)
	total_projects = get_project_count(HTML)
#	print('Всего найдено %d страниц...' % total_pages )
	print('Всего найдено %s проектов...' % total_projects )
	star = time.clock()
	parser(BASE_URL,2)
	stop = time.clock()
	print("End: clock {}".format(stop - star) )
	
	
if  __name__ == "__main__":
	main()
	


