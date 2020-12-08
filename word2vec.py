'''
Word2Vec
 - 분류 등과 같이 별도의 레이블이 없이 텍스트 자체만 있어도 학습이 가능
 - word2vec의 방식 : 주변 단어의 관계를 이용
   -- CBOW(continuous bag-of-word)
      주변 단어의 임베딩을 더해서 대상 단어를 예측
   -- Skip-Gram
      대상 단어의 임베딩으로 주변 단어를 예측
      일반적으로 CBOW보다 성능이 좋은 편
      한번에 여러 단어를 예측해야 하기 때문에 비효율적
      최근에는 negative smapling이라는 방법을 사용
'''
'''
T-SNE (t-Stochastic Neighbor Embedding)
고차원의 벡터들의 구조를 보존하여 저차원으로 사상하는 차원 축소 알고리즘
단어 임베딩에서도 생성된 고차원의 벡터들을 시각화하기 위해 이 T-SNE 알고리즘을 많이 사용
t-SNE는 먼저 원 공간의 데이터 유사도와 임베딩 공간의 데이터 유사도를 정의
t-SNE 학습은 원 공간의 데이터 유사도와 비슷해지도록 임베딩 공간의 위치를 조정하는 것임
'''

from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                             remove=('headers', 'footers', 'quotes'))
documents = dataset.data
print(f"최초 데이터 개수 : {len(documents)}")
# print(documents[5])

## 불필요한 특수문자 등 제거 필요 (데이터 전처리)

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def clean_text(d):
    pattern = r'[^a-zA-Z\s]'  # 알파벳이 아닌 것들은 전부 제거
    text = re.sub(pattern, "", d)
    return text

def clean_stopword(d):
    stop_words = stopwords.words('english')
    return " ".join([w.lower() for w in d.split() if w not in stop_words and len(w) > 3])

def tokenize(d):
    return word_tokenize(d)

import pandas as pd

news_df = pd.DataFrame({'article':documents})
print(f"데이터 프레임 변환후 데이터 개수 : {len(news_df)}")

news_df.replace("", float("NaN"), inplace=True)
news_df.dropna(inplace=True)
# print(len(news_df))

news_df['article'] = news_df['article'].apply(clean_text)
# print(news_df[:5])
news_df['article'] = news_df['article'].apply(clean_stopword)
# print(news_df[:5])
tokenized_news = news_df['article'].apply(tokenize)
tokenized_news = tokenized_news.to_list()
# print(tokenized_news[:5])

import numpy as np

drop_news = [index for index, sentence in enumerate(tokenized_news) if len(sentence) <= 1]
news_texts = np.delete(tokenized_news, drop_news, axis=0)
print(f"전처리후 데이터 개수 : {len(news_texts)}")

#######여기까지가 데이터 전처리, 이후 Word2Vec 만들기 ########

### Gensim을 이용한 Word2Vec##############################
## CBOW 방식 먼저

from gensim.models import Word2Vec
# model = Word2Vec(sentences=news_texts, window=3, size=100, min_count=5, workers=4, sg=0)
## 윈도는 앞뒤로 단어 몇개를 볼 것인가? 워커스는 병렬처리 개수
# result = model.wv.similarity('man', 'woman')
# result = model.most_similar(positive=['soldiers'])
# result = model.most_similar(positive=['man', 'company'], negative=['woman'])
# print(result)

## Skip-gram 방식
# model = Word2Vec(sentences=news_texts, window=3, size=100, min_count=5, workers=4, sg=1)  # 끝에 sg만 1로 바뀜
# result = model.wv.similarity('man', 'woman')
# result = model.most_similar(positive=['soldiers'])
# result = model.most_similar(positive=['man', 'company'], negative=['woman'])
# print(result)


## 임베딩 벡터 시각화
from gensim.models import KeyedVectors

# model.wv.save_word2vec_format('./data/news_w2v')
# 모델을 파일로 다운로드
##!python -m gensim.scripts.word2vec2tensor -i ./data/news_w2v -o ./result/news_w2v
# 다운받을 파일을 텐서, 메타데이터 파일로 변환
## https://projector.tensorflow.org/
# 이사이트로 가서 텐서와 메타데이터 로드후 비쥬얼~


