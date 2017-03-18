# _*_ coding: utf-8 _*_

## 导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读入一个txt文件
text = open('mydata.txt').read()
# 生成词云
wordcloud = WordCloud().generate(text)  # generate表示从文本文件直接生成词云
# generate函数等价于generate_from_text

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
# 保存图片
wordcloud.to_file('text.jpg')
wordcloud.to_html('text.html')
wordcloud.to_image('text')

# 除了直接读入文本生成词云，也可以使用字典格式的词频作为输入
text_dict = {
    'you':2993,'and':6625,'in':2767,'was':2525,'the':7845
}
# generate_from_frequencies表示从词以及其频数生成词云
wordcloud = WordCloud.generate_from_frequencies(text_dict)

# 此时，我们想将词云填充到指定的形状之中，为达到填充指定形状的效果，需要使用 png 格式的图片。
from scipy.misc import imread
bg_pic = imread('my_img.png')  # 读入所要使用的图片
# 配置词云参数
wc = WordCloud(
    # 设置字体
    font_path = 'BeaverScratches.ttf',
    # 设置图片的宽度，高度
    width = 400,
    height = 400,
    # 设置背景色
    background_color = 'white',
    # 允许最大词汇
    max_words = 200,
    # 词云形状
    mask = bg_pic,
    # 最大号字体
    max_font_size = 100,
    # 停止词的使用
    stopwords = [],
    # 设置最小的字体大小
    min_font_size = 4,
    # 设置最大的字体大小
    max_font_size = 20
)
# 生成词云
wc.generate(text)
# 保存图片
wc.to_file('word.jpg')


## 几个例子
# masked wordcloud
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS  # 加载停止词
d = path.dirname(__file__)
# 读取文件
text = open(path.join(d,'alice.txt')).read()
# 读取设置的图片
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(STOPWORDS)   # 设置停止词
stopwords.add('said')       # 添加一个停止词

wc = WordCloud(backgroud_color='white',max_words=2000,mask=alice_mask,stopwords=stopwords)

# 生成词云图
wc.generate(text)

# 保存图片
wc.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()

# 根据图片中的颜色来生成文字的颜色
# http://amueller.github.io/word_cloud/auto_examples/colored.html
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'alice.txt')).read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open(path.join(d, "alice_color.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")
wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# 从图片中生成颜色
image_colors = ImageColorGenerator(alice_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
