from cortical.termsApi import TermsApi
from cortical.textApi import TextApi
from Scraper import url_scraper as scraper
import config
import slate
import json
import pprint

def PDF2txt(pth):
	with open(pth) as f:
		doc = slate.PDF(f)
		return doc

def url2txt(scrp,url):
	scrp.build_soup(url)

def getkw(txt):
	return api.getKeywordsForText(config.RETINA_NAME,txt) 

def gettokens(txt):
	return api.getTokensForText(config.RETINA_NAME,txt)

def getslices(txt):
	return api.getSlicesForText(config.RETINA_NAME,txt)

if __name__=='__main__':
	client = config.client
	#api = TermsApi(client)
	#terms = api.getTerm("en_associative", term="apple", get_fingerprint=True)

	api=TextApi(client)
	scpr=scraper()

	targettxt=(scpr,"www.nutonomy.com")
	candidatetxts=PDF2txt("resume.pdf")

	kwords=[getkw(candidatetxts[i]) for i in range(len(candidatetxts))] 
	tokens=[gettokens(candidatetxts[i]) for i in range(len(candidatetxts))]
	slices=[getslices(candidatetxts[i]) for i in range(len(candidatetxts))]

	for t in kwords:
		pprint.pprint(t)

	for t in tokens:
		pprint.pprint(t)
