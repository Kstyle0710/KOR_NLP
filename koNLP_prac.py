from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")

#
sentence1 = "지갑을가방에넣는다."
sentence2 = "아버지가방에들어가신다."

a = mecab.nouns(sentence1)
print(a)

b = mecab.nouns(sentence2)
print(b)

## 불용어 사전 만들기

# stop_word = "전 난 일 걸 뭐 줄 만 건 분 개 끝 잼 이거 번 중 듯 때 게 내 말 나 수 거 점 것"
# stop_word = stop_word.split(' ')
# print(stop_word)