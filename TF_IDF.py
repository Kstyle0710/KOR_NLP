'''
어휘 빈도-문서 역빈도(TF-IDF) 분석 Term Frequency - Inverse Document Frequency
단순히 빈도수가 높은 단어가 핵심어가 아닌, 특정 문서에서만 집중적으로 등장할 때 해당 단어가 문서의 주제를 잘 담고 있는 핵심이라고 가정
특정 문서에서 특정 단어가 많이 등장하고 그 단어가 다른 문서에서 적게 등장할 때, 그 단어를 특정 문서의 핵심 단어로 간주
어휘 빈도-문서 역빈도는 어휘 빈도와 역문서 빈도를 곱해서 계산
어휘 빈도는 특정 문서에서 특정 단어가 많이 등장하는 것을 의미
역문서 빈도는 다른 문서에서 등장하지 않는 단어 빈도를 의미
TF-IDF를 편리하게 계산할 수 있도록 sklearn tfidfvectorizer를 이용
'''

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = ['Thinsk like a man of action and act like man of thought',
          "Try not to become a man of success but rather try to become a man of value",
          "Give me liberty, or give me death"]

tfidf = TfidfVectorizer(stop_words="english")
bow = tfidf.fit_transform(corpus)

print(bow.toarray())
print(tfidf.vocabulary_)

columns = []
for k, v in sorted(tfidf.vocabulary_.items(), key=lambda item:item[1]):
    # vocab의 두번째 값을 보고 정렬 실시
    columns.append(k)

df = pd.DataFrame(bow.toarray(), columns=columns)
print(df)