

import wordcloud
import jieba
import imageio
    # 导入imageio库中的imead函数，并用这个函数读取本地图片，作为词云形状图片

mk = imageio.imread('wujiaoxing.png')
            
f = open('关于实施乡村振兴战略的意见.txt',encoding='utf-8')
txt=f.read()
txtlist = jieba.lcut(txt)
string = ' '.join(txtlist)

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=15)

w.generate(string)

w.to_file('output6.png')
