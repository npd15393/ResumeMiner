import grammar_check

class Collator:
	def __init__(self,RFullText,WFullText,kw1,t1,kw2=[],t2=[]):
		self.rkeywords=[r for r in kw1]
		self.rtokens=[r for r in t1]
		self.RTexts=[r for r in RFullText]
		self.WTexts=[r for r in WFullText]
		if len(t2)>0 and len(kw2)>0:
			self.wkeywords=[r for r in kw2]
			self.wtoken=[r for r in t2]


	def kwMatch_test(self):
		pass

	def TokenSimilarity_test(self):
		pass#cs

	def Grammar_test(self):
		errors=0
		tool = grammar_check.LanguageTool('en-GB')
		totl=get_prone_no(self.RTexts)
		for ts in self.RTexts:
			text = ts
			matches = tool.check(text)
			errors+=len(matches)
		return 1-errors/totl


	def get_prone_no(self,txts):
		no=0
		for ts in txts:
			e=ts.split()
			no+=(len(e)-1)
		return no

	def getNGrams(self,wordlist, n):
		return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

	def collate(self):
		test1_score=kwMatch_test()
		test2_score=TokenSimilarity_test()
		test3_score=Grammar_test()
		return 0.3*test1_score+0.3*test2_score+0.4*test3_score