from cortical.termsApi import TermsApi
from cortical.textApi import TextApi
from Scraper import url_scraper as scraper
import config
import slate
import json
import pprint
from collator import Collator 

TARGET_COMPANY_URL="https://www.mathworks.com/company/jobs/opportunities/18152-reinforcement-learning-summer-intern"
testing_slate=False
testing_soup=False

def PDF2txt(pth):
	with open(pth) as f:
		doc = slate.PDF(f)
		return doc

def url2txt(scrp,url):
	return scrp.extract_text(url)

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
	kwords=[]
	tokens=[]
	targettxt=url2txt(scpr,TARGET_COMPANY_URL)
	candidatetxts=PDF2txt("resume.pdf")
	for i in range(len(candidatetxts)):
		kwords+=getkw(candidatetxts[i]) 
		tokens+=gettokens(candidatetxts[i])

	print("Keywords extracted, Tokens ready")
	#slices=[getslices(candidatetxts[i]) for i in range(len(candidatetxts))]

	if testing_slate:
		print([r.encode('utf-8') for r in kwords])
		print([r.encode('utf-8') for r in tokens])

	if testing_soup:
		print(str(targettxt))

	cp=Collator(candidatetxts[0],targettxt,kwords,tokens)


	print(str(cp.collate()*10)+' is the resume competency rating out of 10')