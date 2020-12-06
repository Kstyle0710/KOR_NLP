## pip install wordcloud

from wordcloud import WordCloud
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_excel('./result/ko_nlp_1126(3).xlsx')

target = df['형태소']

# print(target)
# print(type(target))
# print(target[0])
# print(type(target[0]))
#
# kim = target[0].split(",")
# print(kim)
# print(type(kim))
# print(kim[0])


total =""
total1 = []

for group in target:
    group = str(group).split(",")

    for word in group:
        total += " ".join(word)+" "
        # total1.append(group)

print(total)

# print(type(total))
# print(total)

wc = WordCloud(background_color = 'white', font_path='./font/NanumGothic.ttf')
wc.generate(total)
# wc.generate_from_frequencies(dict(total))
figure = plt.figure(figsize = (12, 12))
ax = figure.add_subplot(1, 1, 1)
ax.axis('off')
ax.imshow(wc)
plt.show()