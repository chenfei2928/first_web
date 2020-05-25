

import wordcloud
import jieba
import imageio
    # 导入imageio库中的imead函数，并用这个函数读取本地图片，作为词云形状图片

mk = imageio.imread('alice.png')
            
f = open('hamlet.txt',encoding='utf-8')
txt=f.read()

w = wordcloud.WordCloud(background_color='white',
                        mask=mk,
                        contour_width=1,
                        contour_color='steelblue')

w.generate(txt)

w.to_file('output9.png')
