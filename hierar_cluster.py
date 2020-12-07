'''
계층적 군집화
개별 개체들을 유사한 개체나 그룹으로 통합해 군집화를 수행하는 알고리즘
비계층적 군집화와 달리 군집수를 지정하지 않아도 군집화를 할 수 있는 것이 장점
계층적 군집화는 모든 개체간 거리나 유사도가 미리 계산되어 있어야만 하며,
계산 복잡도도 비계층적 군집화보다 큼
'''

'''
Scikit-learn
비계층적 군집화의 일종인 agglomerativeClustering(병합군집)을 이용, 계층적 군집화 실습
병합 군집은 각 개체들을 클러스터로 간주, 종료 조건을 만족할 때까지 가장 비슷한
두 클러스터들을 합치며 진행
병합 군집의 종료 조건에는 3가지를 지정 가능 (무한정 합칠 수는 없으므로)
  1) ward - 모든 클러스터 내의 분산을 가장 적게 증가시키는 두 클러스터를 합침(기본값)
  2) average - 클러스터간 평균 거리가 가장 짧은 두 클러스터를 합침
  3) complete - 클러스터간 최대 거리가 가장 짧은 두 클러스터를 함침
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
# print(results[:10])

## t-sne를 이용한 단어 벡터 시각화
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

word2vec = Word2Vec(results, min_count=5)
print(word2vec)
review1 = word2vec.most_similar('고소차')
print(review1)

tsne = TSNE(n_components=2)   # 2차원으로..
print(tsne)

vocab = word2vec.wv.vocab
similarity = word2vec[vocab]
print(similarity)

transform_similarity = tsne.fit_transform((similarity))
df = pd.DataFrame(transform_similarity, index=vocab, columns=['x', 'y'])
print(df[0:10])

import seaborn as sns
# sns.lmplot('x', 'y', data=df, fit_reg=False, size=8)
# plt.show()

##### ward 방식
# from sklearn.cluster import AgglomerativeClustering
#
# ward = AgglomerativeClustering(n_clusters=6, linkage='ward')
# predict = ward.fit_predict(df)
# print(predict)
#
# result1 = df
# result1['predict'] = predict
# print(result1[0:20])
#
# sns.lmplot('x', 'y', data=result1, fit_reg=False, size=6, hue="predict")
# plt.show()

##### average 방식
# from sklearn.cluster import AgglomerativeClustering
#
# avg = AgglomerativeClustering(n_clusters=6, linkage='average')
# predict = avg.fit_predict(df)
# print(predict)
#
# result1 = df
# result1['predict'] = predict
# print(result1[0:20])
#
# sns.lmplot('x', 'y', data=result1, fit_reg=False, size=6, hue="predict")
# plt.show()

##### complete 방식
# from sklearn.cluster import AgglomerativeClustering
#
# compl = AgglomerativeClustering(n_clusters=6, linkage='complete')
# predict = compl.fit_predict(df)
# print(predict)
#
# result1 = df
# result1['predict'] = predict
# print(result1[0:20])
#
# sns.lmplot('x', 'y', data=result1, fit_reg=False, size=6, hue="predict")
# plt.rcParams['axes.unicode_minus'] = False    # 마이너스 숫자 표기 오류 해소
# plt.show()
