import grammar_check
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class Collator:
	def __init__(self,RFullText,WFullText,kw1,t1):
		self.rkeywords=[r.encode('utf-8') for r in kw1]
		self.rtokens=[r.encode('utf-8') for r in t1]
		self.RTexts=RFullText
		filter(lambda a: a != ' ', WFullText)
		self.WTexts=WFullText
		print("Indexing ready")


	def kwMatch_test(self):
		score=0

		for kws in self.rkeywords:
			for o in self.WTexts:
				if kws == o:
					score+=1
					break
		frac=float(score)#/float(len(self.rkeywords))
		return frac

	def TokenSimilarity_test(self):
		vect = TfidfVectorizer(min_df=1)
		wt=' '.join(self.WTexts)
		tfidf = vect.fit_transform([wt,self.RTexts])
		arr=(tfidf * tfidf.T).A
		return np.sqrt(1-np.linalg.det(arr))

	def Grammar_test(self):
		errors=0
		tool = grammar_check.LanguageTool('en-GB')
		totl=self.get_prone_no(self.rtokens)
		for ts in self.rtokens:
			text = ts
			matches = tool.check(text)
			errors+=len(matches)
		return errors/totl


	def get_prone_no(self,txts):
		no=0
		for ts in txts:
			e=ts.split()
			no+=(len(e)-1)
		return no

	def getNGrams(self,wordlist, n):
		return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

	def sigmoid(self,n):
		return np.exp(n)/(1+np.exp(n))

	def collate(self):
		test1_score=self.kwMatch_test()
		test2_score=self.TokenSimilarity_test()
		#test3_score=self.Grammar_test()

		return max(0.4*self.sigmoid(test1_score)+0.6*test2_score,0)#-0.5*test3_score,0)