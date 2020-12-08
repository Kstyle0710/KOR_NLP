'''
Embedding = Vectorization
  단어를 컴퓨터가 이해하고 효율적으로 처리할 수 있도록 단어를 벡터화 하는 기술
  워드 임베딩을 거쳐 잘 표현된 단어 벡터들은 계산이 가능하며, 모델 투입도 가능함

Encoding
  기계는 자연어를 이해할 수 없기 때문에 데이터를 기계가 이해할 수 있도록 숫자 등으로 변환해주는 작업
  텍스트 처리에서는 주로 정수 인코딩, 원 핫 인코딩을 사용함
'''

# 정수 인코딩
## Dictionary를 이용한 정수 인코딩
## 각 단어와 정수 인덱스를 연결하고, 토큰을 변환해주는 정수 인코딩

text = "평생 살 것처럼 꿈을 꾸어라. 그리고 내일 죽을 것처럼 오늘을 살아라."
tokens = [x for x in text.split(' ')]
# print(tokens)
unique = set(tokens)   # 중복 값 제거
unique = list(unique)   # 리스트로 변환
# print(unique)

token2idx = {}
for i in range(len(unique)):
    token2idx[unique[i]] = i

encoded = [token2idx[x] for x in tokens]
print(encoded)

## keras를 이용한 정수 인코딩 (자동으로 단어 빈도가 높은 단어의 인덱스는 낮게 설정)
# from tensorflow.keras.preprocessing.text import Tokenizer
#
# text = "평생 살 것처럼 꿈을 꾸어라. 그리고 내일 죽을 것처럼 오늘을 살아라."
#
# t = Tokenizer()
# t.fit_on_texts([text])
# print(t.word_index)
#
# encoded = t.texts_to_sequences([text])[0]
# print(encoded)
#

# One Hot Encoding
'''
  조건문과 반복문을 이용한 원 핫 인코딩
   - 원 핫 인코딩은 정수 인코딩한 결과를 벡터로 변환한 인코딩
   - 원 핫 인코딩은 전체 단어 개수 만큼의 길이를 가진 배열에 해당 정수를 가진 위치에는 1, 나머지는 0을 가진 벡터로 변환
'''
import numpy as np
# one_hot = []
# for i in range(len(encoded)):  # 전체 개수만큼 반복
#     temp = []
#     for j in range(max(encoded)):  # (중복 값 고려,) 최대 숫자만큼 반복
#         if j == (encoded[i] - 1):
#             # print(j)
#             # print(encoded[i])
#             temp.append(1)
#         else:
#             temp.append(0)
#     one_hot.append(temp)
# print(np.array(one_hot))

'''
keras를 활용한 원 핫 인코딩
  - keras에서는 정수 인코딩을 원 핫 인코딩으로 간단하게 변환해주는 to_categorical() 함수를 제공
'''
from tensorflow.keras.utils import to_categorical
# one_hot = to_categorical(encoded)
# print(one_hot)



