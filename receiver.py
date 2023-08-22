
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

filepath = "c:/Users/Molson/Desktop/test.png"
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

# print(modpic)
# print(len(modpic))

# # 打印显示
# for i in modpic:
#     print(str('0x{:02x}'.format(int(i))) +',',end='')

stmpath="e:/study/code/mcu/01-1.54EPD显示屏STM32F103C8T6_SPI例程/HARDWARE/OLED/bmp.h"
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
# # 01显示原图片
# with open("c:/Users/Molson/Desktop/display.txt", "w") as f:
#     temp = 0
#     for i in pic:
#         for j in i:
#             f.write( str(j))
#             temp += 1
#             if temp > 199:
#                 f.write('\n')
#                 temp =0
print("代码生成完毕")
    



# # 打开导入图片
# # im = Image.open("c:/Users/Molson/Desktop/test.png").convert('1')
# # 打开图片并使用np转换为数组
# im = np.array(Image.open("c:/Users/Molson/Desktop/test.png").convert(''))
# # 隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
# # 显示图片
# plt.imshow(im)
# plt.show()




# 下面是串口相关的代码
# import serial
# import serial.tools.list_ports
# plist = list(serial.tools.list_ports.comports())
# if len(plist) <= 0:
#     print("The Serial port can't find!")
# else:
#     plist_0 = list(plist[0])
#     serialName = plist_0[0]
#     serialFd = serial.Serial(serialName, 115200, timeout=60)
#     print("check which port was really used >", serialFd.name)
# while(1):
#     line = serialFd.readline() 
#     print(line)




