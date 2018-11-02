



'''Quiz1-2
1.
當positive和negative的樣本數差異過大的情況。
例如target為1的有10個，但target為0的樣本有1000000個，若全部都預測為0，accuracy會超過99%，但事實上根本沒有做出好的預測。

2.
binary fuction在接近零的時候微分不存在，對於gradient decent的學習方法不穩定

3.
模型的bias和variance是指該模型的預測期望誤差和變異數，
假設我們可以實驗無限次重複獲得樣本，每次都訓練一個模型並做預測，實驗的平均物差和變異數就是模型的bias和variance

4.
random forest是一種ensemble的方法，我們希望每一棵樹不太一樣，能夠稍微有一點overfit，都有點極端，但極端的不同，綜合起來就會增加預測準度。
事實上，如果深度設定的過淺或進行樹的修剪，很容易造成每一棵樹太過相似，那random forest的好處就會不明顯。

5.
對於一個有n類的類別變數x，x的數值事實上沒有大小順序意義，因此為了讓類別變數轉成數值變數，
我們可以創造x的one hot encoding，n個binary變數，也就是x=1,x=2,...x=n,n個向量。

6.
Early stopping:設定validation error的early stopping，
regularization:設定模型參數的regularization，(例如L1，L2)
Dropout:設定某些layer的dropout (對於batch trainning這其實算是一種ensemble)'''



'''Quiz 2-1'''

from nltk import FreqDist
from nltk.util import ngrams    

def ngram_probs(filename='D:/raw_sentences.txt'):
	textfile = open(filename)

	bigram_fdist = FreqDist()
	threegram_fdist = FreqDist()

	for line in textfile:
		if len(line) > 1:
			tokens = line.lower().strip().split(' ')

		bigrams = ngrams(tokens, 2)
		bigram_fdist.update(bigrams)
		
		threegrams = ngrams(tokens, 3)
		threegram_fdist.update(threegrams)	
		
	return bigram_fdist,threegram_fdist



def prob3(bigram, cnt2=cnt2, cnt3=cnt3):
	out={}
	temp=0
	n=len(bigram)
	for i, j in enumerate(cnt3):
		cond=0
		for k in range(n):
			cond+=i[k]!==bigram[k]
		if cond==1:
		# if i[0]==bigram[0] & i[1]==bigram[1]:
			out[i[-1]]=j
			temp+=j
	for i, j in enumerate(out):
		out[i]=j/temp
		
	return out
		
def predict_max(starting, cnt2=cnt2, cnt3=cnt3):
	out=[]
	temp=0
	for i, j in enumerate(cnt3):
		if i[0]==bigram[0] & i[1]==bigram[1]:
			if j>temp:
				out=[i[2]]
				temp=j
			elif j==temp:
				out.append(i[2])
	return out
		


def predict_beam(bigram, beam_size=4, sent_length=10, cnt2=cnt2, cnt3=cnt3):
	p=prob3(bigram)
	txt=
	for range(10):
	
		
		

return list_of_sentence



