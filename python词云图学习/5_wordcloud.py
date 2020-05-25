

import wordcloud
import jieba

f = open('丰乳肥臀.txt',encoding='utf-8')
txt=f.read()
txtlist = jieba.lcut(txt)
string = ' '.join(txtlist)

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

w.generate(string)

w.to_file('output555.png')
