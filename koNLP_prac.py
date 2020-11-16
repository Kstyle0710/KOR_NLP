import MeCab
from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")


a = mecab.nouns("아버지가방에들어가신다")
print(a)

