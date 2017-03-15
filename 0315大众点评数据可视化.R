# 对于获取到的大众点评数据，这里使用R中的REmap包进行数据的可视化处理
rm(list=ls())
setwd("C:/Users/jk/Desktop")      #　设置工作目录
library(REmap)
options(digits = 15)
df = read.csv('爬取大众点评数据(含经纬度).csv',stringsAsFactors = F)     # 读取数据
table_1 = table(df$shop_type)                                         # 查看每种类型的餐厅有多少个
# 生成颜色的向量
# 给予相同的菜系赋予相同的颜色，可先将数据按照shop_type升序进行排序，然后再赋值
colors = c()
mycolor = c('#FFC125','#F0FFF0','#CD853F','#BF3EFF','#9932CC',
            '#8B7765','#6E7B8B','#4D4D4D','#00CD66','#00868B',
            '#FF7F50','#F7F7F7','#EED5B7','#EEAEEE','#DEB887',
            '#CDC1C5','red','blue','skyblue','dark')
for (i in 1:length(table_1)){                                 # 对于同一种类型的餐厅赋予相同的颜色标记
  colors = c(colors,rep(mycolor[i],table_1[i]))
}

geoData = df[,c('lng','lat','shop_name')]
colnames(geoData) = c('lon','lat','name')

pointData = data.frame(geoData$name)
pointData$color = colors
colnames(pointData) = c('name','color')

# 值得主要的是，由于部分餐厅的名称中含有'符号，结果会无显示，可通过F12键查找到该餐厅的信息，并给予改正
# 自定义地理样式：
# 加载源代码中的markLineStr、markPointStr、remap函数
# 对于源代码中的remapB函数修改所要的参数，可以将其定义为remapBl函数
remapBl(get_city_coord("上海"),
       zoom = 13,
       color = "Blue",
       title = "上海美食",
       markPointData = pointData,
       markPointTheme = markPointControl(symbol = 'circle',symbolSize = 7,effect = F),
       geoData = geoData)
