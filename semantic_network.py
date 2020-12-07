'''
의미 연결만 분석(Semantic Network Analysis)
일정한 범위 내에서 어휘가 동시에 등장하면 서로 연결된 것으로 간주하고 이 견결 관계들을 분석

어휘 동시 출현 빈도의 계수화
두개 이상의 어휘가 일정한 범위나 거리 내에서 함께 출현하는 것을 의미
단어간의 동시 출현관계를 분석하면 문서나 문장으로부터 두 단어가 유사한 의미를 가졌는지 등의 추상화된 정보를 얻을 수 있음
동시 출현 빈도는 Window라는 지정 범위 내에서 동시 등장한 어휘를 확률 등으로 계수화 가능
nltk에서 제공하는 ConditionalFreqDist 함수를 이용하면 문맥별 단어 빈도를 쉽게 측정 가능
'''


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

from nltk import ConditionalFreqDist, bigrams

bgrams = [bigrams(x) for x in results]

token = []
for i in bgrams:
    token += ([x for x in i])
cfd = ConditionalFreqDist(token)
# print(cfd.conditions())

# print(cfd["장비"]["대량"])  # 두 단어의 동시 출현 빈도수
# print(cfd["용접"].most_common(2))  # 단어와 동시 출현 빈도가 높은 것 00개 출력

import numpy as np

freq_matrix = []
for i in cfd.keys():
    temp = []
    for j in cfd.keys():
        temp.append(cfd[i][j])
    freq_matrix.append(temp)
freq_matrix = np.array(freq_matrix)

# print(cfd.keys())
# print(freq_matrix)

df = pd.DataFrame(freq_matrix, index=cfd.keys(), columns = cfd.keys())
df.style.background_gradient(cmap = 'coolwarm')
# print(df)
# df.to_excel("./result/semantic_network_1207.xlsx", encoding='utf-8-sig')

import networkx as nx

G = nx.from_pandas_adjacency(df)
# print(G.nodes())   # 노드는 각 단어들
# print(G.edges())   # 엣지는 관계들
# print(G.edges()[('소방', '습식')])
# print(G.edges()[('용접', '수동')])

# nx.draw(G, with_labels=True)
# plt.show()

## 어휘 동시 출현 확률 계산에는 nltk의 ConditionalProbDist 이용 가능

from nltk.probability import ConditionalProbDist, MLEProbDist

cpd = ConditionalProbDist(cfd, MLEProbDist)
# print(cpd.conditions())

prob_matrix = []
for i in cpd.keys():
    prob_matrix.append([cpd[i].prob(j) for j in cpd.keys()])

prob_matrix = np.array(prob_matrix)
print(cpd.keys())
print(prob_matrix)

df = pd.DataFrame(prob_matrix, index=cpd.keys(), columns=cpd.keys())
df.style.background_gradient(cmap = 'coolwarm')
# print(df)
# df.to_excel("./result/semantic_network_prob_1207.xlsx", encoding='utf-8-sig')

G = nx.from_pandas_adjacency(df)
print(nx.degree_centrality(G))  # 연결중심성 출력






