## 불용어 제거
import MeCab
import pandas as pd
from tqdm import tqdm
import time
from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")


df = pd.read_excel('./data/data1.xlsx')
target = df["작업행동"]

targets =[]

results = []

stop_word = "전 난 일 걸 뭐 줄 만 건 분 개 끝 잼 이거 번 중 듯 때 게 내 말 나 수 거 점 것 등 측 의 급 후 간 단 시 곳"
stop_word = stop_word.split(' ')
# print(stop_word)


##########  문제 있음
for sentence in tqdm(target):
    result = []
    for noun in mecab.nouns(sentence):
        if noun not in stop_word:
            result.append(noun)
    targets.append(sentence)
    results.append(result)


summary = [targets, results]

result_df = pd.DataFrame(summary)
result_df = result_df.T
print(result_df.head(20))

result_df.to_excel("./result/ko_nlp_1126(3).xlsx", encoding='utf-8-sig')

