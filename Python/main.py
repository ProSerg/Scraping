#!/usr/bin/env python3


# working with network
import urllib.request
#
import time
import string
import urllib3
 
# parsing HTML
from bs4 import BeautifulSoup
#
from datetime import datetime
from datetime import date
"""
ПО дате лучше не ориентироваться. Странная система на сайте.
"""

BASE_URL = 'https://www.weblancer.net'
PROJECTS_URL = 'https://www.weblancer.net/jobs/?type=project'

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
	http = urllib3.PoolManager()
	for number in range(1, count + 1) :
		html = get_html(url+"&page={}".format(number))
		soup = BeautifulSoup( html, "lxml" )
		rows = soup.find('div', class_='container-fluid cols_table show_visited' )
		for row in rows:
			title = row.find('a', class_ = "title" ).text
			amount = row.find('div', class_ = "col-sm-2 amount title" ).text.strip()
			categories = row.find_all('a', class_ = "text-muted" )
			link = row.find('a', class_ = "title" )["href"]
			
			date = row.find('span', class_ = "time_ago" )['title']
			date_object = datetime.strptime( date, '%d.%m.%Y в %H:%M')
			date_delta = date_today - date_object
			days = date_delta.days
			hours = date_delta.seconds/3600
			minutes = date_delta.seconds/3600/3600
			
			#print("ROW:{}".format(row))
			print("Title: %s" % title )
			if amount:
				print("Amount: %s" % amount )
			else:
				print("Amount: ---" )
			
			if days > 0:
				print("Date: %d dayes" % days )
			else:
				print("Date: %.1f hours" % hours )
			name_vategories = ""
			#for category in categories:
			#	name_vategories = name_vategories + category.text
			name_vategories = ", ".join(["%s" % (category.text) for category in  categories])	
			print("Category: %s" % name_vategories )
			print("Link: %s" % link )
#			page = http(BASE_URL + link)
			#r = http.request('GET', BASE_URL + link)
			#txt = r.data.decode('windows-1252')
			#print(txt)
## участок кода для получения содержимого
			ht = get_html(BASE_URL + link)
			sp = BeautifulSoup( ht, "lxml" )
			#objs = sp.find_all('div', class_='col-sm-12' )
			#objs = sp.select( 'div.col-sm-12:nth-child(2)' )
			objs = sp.select( 'div.col-sm-12 + div.col-sm-12' )
			#for obj in objs:
			#if len(objs) > 1:
			if objs:
				#print(objs.text.strip())
				print(objs.text)
			#print(sp.read())
			#print( "{}".format( page.read() )
			print(" ")
	
def main():
	HTML = get_html(PROJECTS_URL)
#	total_pages = get_page_count(HTML)
	total_projects = get_project_count(HTML)
#	print('Всего найдено %d страниц...' % total_pages )
	print('Всего найдено %s проектов...' % total_projects )
	star = time.clock()
	parser(PROJECTS_URL,2)
	stop = time.clock()
	print("End: clock {}".format(stop - star) )
	
	
if  __name__ == "__main__":
	main()
	


