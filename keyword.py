'''
Keyword Analysis
핵심어 분석이란 불용어 제거와 어간 추출 및 형태소 분석 등의 자연어 처리를 시행한 후 텍스트에서 많이 등장하는
형태소의 등장 빈도를 분석함으로써 핵심어를 추출
특정 텍스트 자료에 많이 나타나는 형태소가 그 텍스트 주제를 표출할 가능성이 높다는 가정에 기초
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
            results.append(noun)
# print(results[:10])

from collections import Counter

nouns_counter = Counter(results)
top_words = dict(nouns_counter.most_common(100))
print(top_words)

# import numpy as np
#
# y_pos = np.arange(len(top_words))
# plt.figure(figsize=(12, 12))
# plt.barh(y_pos, top_words.values())
# plt.title('Word Count')
# plt.yticks(y_pos, top_words.keys())
# plt.show()

##################################

from wordcloud import WordCloud

wc = WordCloud(background_color='white', font_path=fontpath)
wc.generate_from_frequencies(top_words)

figure = plt.figure(figsize=(12, 12))
ax = figure.add_subplot(1, 1, 1)
ax.axis('off')
ax.imshow(wc)
plt.show()


#######################
##!pip install squarify
# import squarify
#
# norm = mpl.colors.Normalize(vmin=min(top_words.values()),
#                             vmax=max(top_words.values()))
# colors = [mpl.cm.Blues(norm(value)) for value in top_words.values()]
# squarify.plot(label=top_words.keys(),
#               sizes=top_words.values(),
#               color=colors,
#               alpha=.7);
# plt.show()
