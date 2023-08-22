
# 导入包
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import cv2
import os
import sys
from PIL import Image

# 是否翻转黑白
Color_flip = 0

# 文件路径
filepath = ""
file_temp = "resized.bmp"

# 图片缩放
image = cv2.imread(filepath)
pic = cv2.resize(image,dsize=(200,200))
cv2.imwrite(file_temp,pic)
pic = cv2.imread(file_temp,cv2.IMREAD_GRAYSCALE)
os.remove (file_temp)

# 显示图片
cv2.imshow("确认图片",pic)
cv2.waitKey(0)
# plt.imshow(pic) 

if Color_flip:
    pic = np.where(pic>128,1,0)
else:
    pic = np.where(pic>128,0,1)
# for i in pic:
#     print(i)
modpic = []
for j in range(0,25):
    for i in range(0,200):
        temp = 0
        for k in range(0,8) :
            temp = temp >> 1
            temp+=(pic[k+j*8][i]) * 0x80
        modpic.append(temp)

stmpath="bmp.h"
# 写入到文档
with open(stmpath, "w") as f:

    f.write(str('''#ifndef __BMP_H\n#define __BMP_H\nconst unsigned char gImage_1[] = { \n'''))
    
    temp = 0
    for i in modpic:
        f.write( str(str('0x{:02x}'.format(int(i))) +','))
        temp += 1
        if temp > 50:
           f.write('\n')
           temp =0

    f.write(str('''\n};\n#endif\n'''))
print("代码生成完毕")
    




