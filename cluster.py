'''
군집분석(cluster Analysis)
군집분석은 데이터의 특성에 따라 유사한 것끼리 묶음
유사성을 기반으로 군집을 분류하고, 군집에 따라 유형별 특징을 분석하는 기법
텍스트에 대한 군집분석에서는 군집으로 묶여진 텍스트들끼리는 최대한 유사하고,
다른 군집으로 묶여진 텍스트들과는 최대한 유사하지 않도록 분류
'''

'''
텍스트 유사도
텍스트 쌍에 대한 자카드 유사도와 코사인 유사도 계산
자카드 유사도 : 두 텍스트 문서 사이에 공통된 용어의 수와 해당 텍스트에 존재하는 총 고유 용어 수의 비율을 사용
코사인 유사도 : 백터 표현 사이의 각도에 대한 코사인 값을 가용. BoW와 TF-IDF행렬은 텍스트에 대한 백터 표현으로 활용 가능
'''
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


## 자카드 유사도 연습
def jaccard_simliarity(d1, d2):
    lemmatizer = WordNetLemmatizer()

    words1 = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(d1)]
    words2 = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(d2)]

    inter = len(set(words1).intersection(set(words2)))
    union = len(set(words1).union(set(words2)))

    return inter/union

d1 = "Think like a man of action and act like man of thought."
d2 = "Try not to become a mae of success but rather try to become a man of value."
d3 = "Give me liberty or give me death"

# print(jaccard_simliarity(d1, d2))
# print(jaccard_simliarity(d1, d3))
# print(jaccard_simliarity(d2, d3))

## 코사인 유사도 연습
tiv = TfidfVectorizer()
corpus = [d1, d2, d3]

tfidf = tiv.fit_transform(corpus).todense()
# print(cosine_similarity(tfidf[0], tfidf[1]))
# print(cosine_similarity(tfidf[0], tfidf[2]))
# print(cosine_similarity(tfidf[1], tfidf[2]))

## 한글 분석

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from tqdm import tqdm
from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")


## 폰트 설정
import matplotlib.font_manager as fm
fontpath = './font/NanumGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=10)
plt.rc('font', family="NanumGothic")
mpl.font_manager._rebuild()


df = pd.read_excel('./data/data1.xlsx')
target = df["작업행동"]

targets =[]
results = []

stop_word = "전 난 일 걸 뭐 줄 만 건 작업 분 위 개 끝 송 잼 이거 부 동 번 중 듯 차 때 게 내 말 나 수 거 점 것 등 측 의 급 후 간 단 시 곳"
stop_word = stop_word.split(' ')

##########
for sentence in tqdm(target):
    result = []
    for noun in mecab.nouns(sentence):
        if noun not in stop_word:
            result.append(noun)
    results.append(result)
print(results[:10])

## Word2Vec 생성
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager as fm
from matplotlib import rc

word2vec = Word2Vec(results, min_count=5)
print(word2vec)
review1 = word2vec.most_similar('고소차')
print(review1)

## t-sne를 이용한 단어 벡터 시각화
tsne = TSNE(n_components=2)   # 2차원으로..
print(tsne)

vocab = word2vec.wv.vocab
similarity = word2vec[vocab]
print(similarity)

transform_similarity = tsne.fit_transform((similarity))
df = pd.DataFrame(transform_similarity, index=vocab, columns=['x', 'y'])
print(df[0:10])

import seaborn as sns
sns.lmplot('x', 'y', data=df, fit_reg=False, size=8)
plt.show()




