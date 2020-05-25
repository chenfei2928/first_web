

import wordcloud

f = open('关于实施乡村振兴战略的意见.txt',encoding='utf-8')
txt=f.read()

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

w.generate(txt)

w.to_file('output3.png')
