# with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
#     file_data = f.readlines()
# print(file_data)

# pip install jamo  ## 종성 여부를 판단하기 위한 라이브러리
#############################

from jamo import h2j, j2hcj

def get_jongsung_TF(sample_text):
    sample_text_list = list(sample_text)
    last_word = sample_text_list[-1]
    last_word_jamo_list = list(j2hcj(h2j(last_word)))
    last_jamo = last_word_jamo_list[-1]
    jongsung_TF = "T"
    if last_jamo in ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅘ', 'ㅚ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅢ', 'ㅐ,ㅔ', 'ㅟ', 'ㅖ', 'ㅒ']:
        jongsung_TF = "F"
    return jongsung_TF


with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
    file_data = f.readlines()
## 추가할 단어 리스트
word_list = ['각장', '결품', '히팅기', '샤클', '레버풀러', '선탑재', '보강빔', '입고' '이동', '횡이송', '버티칼', '그라인딩',
             '론지', '이동용', '가열', '파렛팅', '촌법', '곡외판', '곡형강', '반출', '백히팅', '결품', '권상', '팔렛트'
             '불량부', '턴오버', '탑재', '판계', '후레시', '워셔', '스트레이너', "유볼트", '정리정돈', '재현기'
             '플라즈마', '마그네트', '손수레', '척조오', '이송', '길이', '스페너', '유니버셜', '파렛트', '옵셋', '공냉',
             '크리닝', '블라스팅', '건도막', '신너', '내부재', '내업', '외업', '철의장품', '블라스팅', '믹싱', "미끌", '에어',
             '고소차', '시져스', '재조정', '스크류', '가견투', '텔레스코핑', '블로윙', '에어리스', '맨홀', '래싱', '사운딩',
             '집크레인', '엔진룸', '절차서', '입회', '가압', '설계부', '베터리', '커미셔닝', '미점검', '로드뱅크', '벨브',
             '가스선', '인터락', '구리스', '라이싱', '솔벤트', '용접복', '아웃트리거', '주수량', '주의사항', '송급', '골재부',
             '동담금', '백킹재', '단책', '얼라인', '브라켓', '폴리싱', '인계품', '동파이프', '찬넬', '젠다이', '건조',
             '에어컴프레셔', '플렌지', '볼팅', '그라인드', "밴딩", '바인드', '멀티코어', '융착', '드레인', '입고', "충진", '판계판',
             '소조판', '소부재', '압조절', '와이어링', '컴파운드', '직송재', '주유차','유류차', '부재']

for word in word_list:
    jongsung_TF = get_jongsung_TF(word)
    line = '{},,,,NNP,*,{},{},*,*,*,*,*\n'.format(word, jongsung_TF, word)

    file_data.append(line)


##
with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f:
    for line in file_data:
        f.write(line)

###
with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
    file_new = f.readlines()

print(file_new)

#######################################

# from konlpy.tag import Mecab
#
# mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
# word_list = ['가짜 샤링기 기사', "가우징 기술"]
#
# for word in word_list:
#     print(mecab.pos(word))





