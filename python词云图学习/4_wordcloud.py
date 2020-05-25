
# 同济大学介绍

import wordcloud
import jieba

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')


f = open('同济大学.txt',encoding='utf-8')
txt = f.read()

txtlist = jieba.lcut(txt)
string = ' '.join(txtlist)

w.generate(string)

w.to_file('output4.png')

