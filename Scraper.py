from bs4 import BeautifulSoup as bs
import urllib2
import requests


class url_scraper:
	def __init__(self):
		pass

	def build_soup(self,url):	
		ur=url
		url=requests.get(ur)
		#response = urllib2.urlopen(url)
		#page = response.read()
		soup = bs(url.content,"lxml")
		return soup
