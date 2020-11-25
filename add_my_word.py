# with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
#     file_data = f.readlines()
# print(file_data)

# pip install jamo  ## 종성 여부를 판단하기 위한 라이브러리
#############################

# from jamo import h2j, j2hcj
#
# def get_jongsung_TF(sample_text):
#     sample_text_list = list(sample_text)
#     last_word = sample_text_list[-1]
#     last_word_jamo_list = list(j2hcj(h2j(last_word)))
#     last_jamo = last_word_jamo_list[-1]
#     jongsung_TF = "T"
#     if last_jamo in ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅘ', 'ㅚ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅢ', 'ㅐ,ㅔ', 'ㅟ', 'ㅖ', 'ㅒ']:
#         jongsung_TF = "F"
#     return jongsung_TF
#
#
# with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
#     file_data = f.readlines()
#
# word_list = ['가우징', '샤링기']   ## 추가할 단어 리스트
#
# for word in word_list:
#     jongsung_TF = get_jongsung_TF(word)
#     line = '{},,,,NNP,*,{},{},*,*,*,*,*\n'.format(word, jongsung_TF, word)
#
#     file_data.append(line)
#
#
# ##
# with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f:
#     for line in file_data:
#         f.write(line)
#
# ###
# with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
#     file_new = f.readlines()
#
# print(file_new)

#######################################

from konlpy.tag import Mecab

mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
word_list = ['가짜 샤링기 기사', "가우징 기술"]

for word in word_list:
    print(mecab.pos(word))





