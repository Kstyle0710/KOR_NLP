## 불용어 제거
import MeCab
import pandas as pd
from tqdm import tqdm
import time
from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")


df = pd.read_excel('./data/data2.xlsx')
target = df["대상정보"]

targets =[]
results = []

stop_word = "전 난 일 걸 뭐 줄 만 건 분 개 끝 잼 이거 번 중 듯 때 게 내 말 나 수 거 점 것"
stop_word = stop_word.split(' ')
# print(stop_word)


##########  문제 있음
for i in tqdm(target):
    noun = mecab.nouns(i)
    if noun not in stop_word:
        targets.append(i)
        results.append(noun)

summary = [targets, results]

result_df = pd.DataFrame(summary)
result_df = result_df.T
# print(result_df)

result_df.to_excel("./result/ko_nlp_1123(2).xlsx", encoding='utf-8-sig')
####??
#
# for review in reviews:
#     for noun in mecab.nouns(review):
#         if noun not in stop_word:
#             noun.append(noun)

