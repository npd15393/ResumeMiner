from bs4 import BeautifulSoup as bs
import requests
import re

class url_scraper:
	def __init__(self):
		pass

	def extract_text(self,ur):
		url=requests.get(ur)	
		soup = bs(url.content,"lxml")
		x = str(soup.find_all('p'))
		page = str(re.sub("<.*?>", "", x))
		return page
