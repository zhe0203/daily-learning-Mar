# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import os,sys

# 随机字母
def rndchar():
    return chr(random.randint(65,90))

# 随机颜色1
def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色2
def rndcolor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 240*60
width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))

# 创建Font对象
font = ImageFont.truetype('ariblk.ttf',40)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndcolor())
# 输出文字
for t in range(4):
    draw.text((60*t+10,10),rndchar(),font=font,fill=rndcolor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

# 打开图像文件使用open
im = Image.open('code.jpg')
# im.show()                           # 显示图片
print(im.format, im.size, im.mode)    # 查看图片的属性

# Convert files to JPEG
for infile in sys.argv[1:]:
    f,e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('cannot convert',infile)

# create jpeg thumnails
size = (128,128)
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + '.thumbnail'
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile,'JPEG')
        except IOError:
            print('cannot creat thumbnail for',infile)

# identify image files
for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile,im.format,'%dx%d' % im.size,im.mode)
    except IOError:
        pass

# Cutting, pasting, and merging images

box = (20,10,70,70)   # (left, upper, right, lower)
im = Image.open('1.jpg')
print(im.size)
region = im.crop(box)    # 从图片中截图矩阵大小的图像
# region.show()          # 查看图片
# region.save('crop.jpg','jpeg')

# region = region.transpose(Image.ROTATE_180)    # 将截取的图片旋转180度
# region.show()

box = (30,20,80,80)        # paste函数中的box是按照指定的位置将截取的图片复制
im.paste(region, box)      # 将截取的图片和原图片合并在一起

# rolling an image
def roll(image,delta):
    "Roll an image sideways"
    xsize,ysize = image.size
    delta = delta % xsize
    if delta == 0:return image
    part1 = image.crop((0,0,delta,ysize))
    part2 = image.crop((delta,0,xsize,ysize))
    part1.load()
    part2.load()
    image.paste(part2,(0,0,xsize-delta,ysize))
    image.paste(part1,(xsize-delta,0,xsize,ysize))
    return image

r,g,b = im.split()               # 将图片的颜色取出
im = Image.merge('RGB',(b,g,r))

# Geometrical transforms
im = Image.open('1.jpg')
out = im.resize((128,128))    # 重新设置图片的大小
out = im.rotate(45)           # 逆时针旋转45度
out = im.transpose(Image.FLIP_LEFT_RIGHT)   # 图片左右对换
out = im.transpose(Image.FLIP_TOP_BOTTOM)   # 图片上下对转
out = im.transpose(Image.ROTATE_90)         # 旋转90度
out = im.transpose(Image.ROTATE_180)        # 旋转180度
out = im.transpose(Image.ROTATE_270)        # 旋转270度

# 将图片转换为不同的色彩模式
im = Image.open('1.jpg').convert('L')

# 图像增强
out = im.filter(ImageFilter.DETAIL)

# applying point transforms
im = Image.open('1.jpg')
out = im.point(lambda i:i * 1.1)   # 增加图片的亮度，作用于每一个点

source = im.split()
R,G,B = 0,1,2
mask = source[R].point(lambda i:i<100 and 255) # 选择红色小于100的点
out = source[G].point(lambda i:i*0.7)
source[G].paste(out,None,mask)
im = Image.merge(im.mode,source)

# adjust contrast, brightness, color balance and sharpness in this way.
from PIL import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show('30% more contrast')
