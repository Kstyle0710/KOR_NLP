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


for i in tqdm(target):
    a = mecab.nouns(i)
    targets.append(i)
    results.append(a)

summary = [targets, results]

result_df = pd.DataFrame(summary)
result_df = result_df.T
# print(result_df)

result_df.to_excel("./result/ko_nlp_1116.xlsx", encoding='utf-8-sig')



