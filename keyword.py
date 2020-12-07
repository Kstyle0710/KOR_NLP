'''
Keyword Analysis
핵심어 분석이란 불용어 제거와 어간 추출 및 형태소 분석 등의 자연어 처리를 시행한 후 텍스트에서 많이 등장하는
형태소의 등장 빈도를 분석함으로써 핵심어를 추출
특정 텍스트 자료에 많이 나타나는 형태소가 그 텍스트 주제를 표출할 가능성이 높다는 가정에 기초


'''
## 불용어 제거
import pandas as pd
from tqdm import tqdm
from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")


df = pd.read_excel('./data/data1.xlsx')
target = df["작업행동"]

targets =[]
results = []

stop_word = "전 난 일 걸 뭐 줄 만 건 분 개 끝 잼 이거 번 중 듯 때 게 내 말 나 수 거 점 것 등 측 의 급 후 간 단 시 곳"
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
top_words = dict(nouns_counter.most_common(50))
print(top_words)



