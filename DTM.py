'''
DTM Document Term Matrix  문서에 등장하는 여러 단어들의 빈도를 행렬로 표현
'''

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# corpus = ['Think like a man of action and act like man of thought',
#           "Try not to become a man of success but rather try to become a man of value",
#           "Give me liberty, or give me death"]
# vector = CountVectorizer(stop_words="english")

corpus = ['회사는 울산에 있습니다.' '회사는 현대입니다.' '어제 물건을 가져왔습니다.']
# ko_stop = ['회사는', '에', '회사의', '를', '을', '은']
vector = CountVectorizer()

bow = vector.fit_transform(corpus)

print(bow.toarray())
print(vector.vocabulary_)

columns = []
for k, v in sorted(vector.vocabulary_.items(), key=lambda item:item[1]):
    # vocab의 두번째 값을 보고 정렬 실시
    columns.append(k)

df = pd.DataFrame(bow.toarray(), columns=columns)
print(df)