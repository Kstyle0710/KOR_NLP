#================
import pandas as pd
from tqdm import tqdm
import nltk
from nltk.tokenize import RegexpTokenizer
from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
nltk.download('punkt')


df = pd.read_excel('./data/작업표준 목록_조선외.xlsx')
target = df["표준서명"]

targets =[]

results = []

stop_word = "전 난 일 걸 뭐 줄 만 건 작업 분 위 개 끝 송 잼 이거 부 동 번 중 듯 차 때 게 내 말 나 수 거 점 것 등 측 의 급 후 간 단 시 곳"
stop_word = stop_word.split(' ')
# print(stop_word)

##########
for sentence in tqdm(target):
    result = []
    tokenizer = RegexpTokenizer("[\w]+")
    tokens = tokenizer.tokenize(sentence)
    for token in tokens:
        if token not in stop_word:
            result.append(token)
    targets.append(sentence)
    results.append(result)

# summary = [targets, results]
# result_df = pd.DataFrame(summary)
# result_df = result_df.T
# print(result_df.head(20))
# result_df.to_excel("./result/ko_nlp_1214(1).xlsx", encoding='utf-8-sig')
df["tokenized"] = results
# df.to_excel("./result/ko_nlp_1214(2).xlsx", encoding='utf-8-sig')
print(df.head())
i = '기계가공부'
t1 = df.loc[df["기안자"] == i, ['tokenized']]
print(t1.head())
print()

t1.values.tolist()
print("-"*20)
print(type(t1))
for t2 in t1[:5]:
    print(t2)


### 부서별 토큰 그룹핑
# print("부서별 토큰 통합하기")
# final ={}
# depts = df["기안자"].unique()
# print(depts)
# for i in depts[:1]:
#     print(i)
#     temp_list =[]
#     for j in df.loc[df["기안자"] == i, ['tokenized']]:
#         print(j)
#         for m in j:
#             if m not in temp_list:
#                 temp_list.append(m)
#             else:
#                 pass
#
#     final[j] = temp_list
# print(final)
