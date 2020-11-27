## pip install wordcloud

from wordcloud import WordCloud
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_excel('./result/ko_nlp_1124.xlsx')

target = df['형태소']

# print(target)
# print(type(target))


total =""

for group in target:
    group = group.strip("][").split(",")

    for word in group:
        word = word.strip("'").strip(" '")
        total += " ".join(word)+ " "

# print(type(total))
# print(total)

wc = WordCloud(background_color = 'white', font_path='./font/NanumGothic.ttf')
wc.generate(total)

figure = plt.figure(figsize = (12, 12))
ax = figure.add_subplot(1, 1, 1)
ax.axis('off')
ax.imshow(wc)
plt.show()