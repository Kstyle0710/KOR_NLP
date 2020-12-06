from konlpy.tag import Okt
from collections import Counter
import pandas as pd


df = pd.read_excel('./result/ko_nlp_1126(3).xlsx')

target = df['형태소']

okt = Okt()
noun = okt.nouns(target)
count = Counter(target)

noun_list = count.most_common(100)
for v in noun_list:
    print(v)
