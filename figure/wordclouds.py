from scipy.misc import imread
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
from os import path

def draw_wordcloud(txt):
    #读入一个txt文件,基于此文本知错词云图
    color_mask = imread("f1.jpg")  # 读取背景图片，
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码，文件名不支持中文
        font_path="STKAITI.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色，默认为黑，可根据需要自定义为颜色
        background_color='black',
        #词云形状，
        mask=color_mask,
        #允许最大词汇
        max_words=400,
        #最大号字体，如果不指定则为图像高度
        max_font_size=100,
        #画布宽度和高度，如果设置了msak则不会生效
        width=600,
        height = 400,
        margin = 2,
        #词语水平摆放的频率，默认为0.9.即竖直摆放的频率为0.1
        prefer_horizontal = 0.8
    )
    wc = cloud.generate_from_frequencies(txt) #产生词云
    #wc = cloud.fit_words(txt) 跟以上是同一意思
    wc.to_file("weibo_cloud2.jpg") #保存图片
    #显示词云图片
    plt.imshow(wc)
    #不现实坐标轴
    plt.axis('off')
    #绘制词云
    #plt.figure(dpi = 600)
    image_colors = ImageColorGenerator(color_mask)
    #plt.imshow(wc.recolor(color_func=image_colors)) 重新上色，
    plt.show()

if __name__ == '__main__':
    i=0
    dict = {}
    blogs = pd.read_csv('word_count.txt', header=None, sep=' ',
                        encoding='utf-8')

    while(i<100):
        line = blogs.ix[i]
        dict[line.values[0]] = float(line.values[1])
        i=i+1

    draw_wordcloud(dict)