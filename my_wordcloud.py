## pip install wordcloud

from wordcloud import WordCloud
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_excel('./result/ko_nlp_1125(2).xlsx')

target = df['target']
print(type(target))

total = []

# # print(len(target))
#
for i in target:
    a = i.strip('][').split(',')
    total = total + a
print(total)


# wc = WordCloud(background_color = 'white', font_path='./font/NanumGothic.ttf')
# wc.generate_from_frequencies(total)
#
# figure = plt.figure(figsize = (12, 12))
# ax = figure.add_subplot(1, 1, 1)
# ax.axis('off')
# ax.imshow(wc)
# plt.show()