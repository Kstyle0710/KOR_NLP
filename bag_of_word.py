## pip install sklearn

from sklearn.feature_extraction.text import CountVectorizer

## 영문 일반
corpus = ['think like a man of action and act like man of thought']
vector = CountVectorizer()
bow = vector.fit_transform(corpus)
print(bow.toarray())
print(vector.vocabulary_)

## 영문 stop word 제거
corpus = ['think like a man of action and act like man of thought']
vector = CountVectorizer(stop_words='english')
bow = vector.fit_transform(corpus)
print(bow.toarray())
print(vector.vocabulary_)

## 한글 적용
# corpus = ['올해 부동산 등 자산 가격 상승의 여파로 소득 상위 10% 가구의 부동산 자산이 작년보다 증가했다.']
# vector = CountVectorizer()
# bow = vector.fit_transform(corpus)
# print(bow.toarray())
# print(vector.vocabulary_)
#
# ## Mecab 형태소 사전 적용
# import re
# from konlpy.tag import Mecab
# tagger = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
#
#
# corpus = '올해 부동산 등 자산 가격 상승의 여파로, 소득 상위 10% 가구의 부동산 자산이 작년보다 증가했다.'
# tokens = tagger.nouns(re.sub("(\.)", "", corpus))
#
# vocab = {}
# bow = []
#
# for tok in tokens:
#     if tok not in vocab.keys():
#         vocab[tok] = len(vocab)
#         bow.insert(len(vocab)-1, 1)
#     else:
#         index = vocab.get(tok)
#         bow[index] = bow[index] + 1
# print(bow)
# print(vocab)
#
