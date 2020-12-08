'''
keras 이용 word2vec
'''

## 데이터 가져오기
from sklearn.datasets import fetch_20newsgroups
dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                             remove=('header', 'footer', 'quotes'))
documents = dataset.data
print(f"최초 데이터 개수 : {len(documents)}")
# print(documents[1])

## 데이터 전처리 하기
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt')

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

news_df['article'] = news_df['article'].apply(clean_text)
# print(news_df[:5])
news_df['article'] = news_df['article'].apply(clean_stopword)
# print(news_df[:5])
tokenized_news = news_df['article'].apply(tokenize)
tokenized_news = tokenized_news.to_list()

import numpy as np

drop_news = [index for index, sentence in enumerate(tokenized_news) if len(sentence) <= 1]
news_texts = np.delete(tokenized_news, drop_news, axis=0)
print(f"전처리후 데이터 개수 : {len(news_texts)}")
# print(news_texts[2])

## 전처리 완료후 분석
from tensorflow.keras.preprocessing.text import Tokenizer
news_2000 = news_texts[:2000]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(news_2000)

idx2word = {value:key for key, value in tokenizer.word_index.items()}
sequences = tokenizer.texts_to_sequences(news_2000)

vocab_size = len(tokenizer.word_index)+1
print(vocab_size)
print(sequences[0])

'''
Skip-gram 전처리
   네거티브 샘플링 (Negative Sampling)
     word2vec은 출력층이 내놓는 값이 소프트맥스 함수를 적용해 확률값으로 변환한 후 이를 정답과 비교해 역전파
     소프트맥스를 적용하려면 분모에 해당하는 값, 즉 중심단어와 나머지 모든 단어의 내적을 한 뒤, 다를 다시 exp 계산을
     하는데 전체 단어가 많은 경우 엄청난 계산량 발생
     네거티브 샘플링은 소프트맥스 확률을 구할 때 전체 단어를 대상으로 구하지 않고, 일부 단어만 뽑아서 계산을 하는 방식
     네거티브 샘플링 동작은 사용자가 지정한 윈도우 사이즈 내에 등장하지 않는 단어(negative samples)를
     5~20개 정도 뽑고 이를 정답 단어와 합쳐 전체 단어처럼 소프트맥스 활률을 계산하여 파라미터 업데이트
'''
from tensorflow.keras.preprocessing.sequence import skipgrams

## 10개 샘플로 먼저 시도

# skip_grams = [skipgrams(sample, vocabulary_size=vocab_size, window_size=10) for sample in sequences[:10]]
# pairs, labels = skip_grams[0][0], skip_grams[0][1]
# for i in range(5):
#     print("{:s}({:d}), {:s}({:d}) -> {:d}".format(
#         idx2word[pairs[i][0]], pairs[i][0],
#         idx2word[pairs[i][1]], pairs[i][1],
#         labels[i]))

## 전체 데이터로 시도
skip_grams = [skipgrams(sample, vocabulary_size=vocab_size, window_size=10) for sample in sequences]

## 모델 생성
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Embedding, Reshape, Activation, Input, Dot
from tensorflow.keras.utils import plot_model

embed_size = 50

### 이후로는 너무 어려워서 중단


