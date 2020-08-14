import cv2
import numpy as np
import random
import math

#增加饱和度光照的噪声
def tfactor(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hsv[:,:,0] = hsv[:,:,0]*(0.8+ np.random.random()*0.2)
    hsv[:,:,1] = hsv[:,:,1]*(0.3+ np.random.random()*0.7)
    hsv[:,:,2] = hsv[:,:,2]*(0.2+ np.random.random()*0.8)

    img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    return img

#随机数
def r(val):
    return int(np.random.random() * val)

#图像均值平滑滤波
def AddGauss(img, level):
    level=r(level)
    return cv2.blur(img, (level * 2 + 1, level * 2 + 1))

def AddNoiseSingleChannel(single):
    diff = 255-single.max()
    noise = np.random.normal(0,1+r(100),single.shape)
    noise = (noise - noise.min())/(noise.max()-noise.min())
    noise= diff*noise
    noise= noise.astype(np.uint8)
    dst = single + noise
    return dst

def addNoise(img):
    img[:,:,0] =  AddNoiseSingleChannel(img[:,:,0])
    img[:,:,1] =  AddNoiseSingleChannel(img[:,:,1])
    img[:,:,2] =  AddNoiseSingleChannel(img[:,:,2])
    return img
def rotRandrom(img, factor, size):
#添加透视畸变
    shape = size
    pts1 = np.float32([[0, 0], [0, shape[0]], [shape[1], 0], [shape[1], shape[0]]])
    pts2 = np.float32([[r(factor), r(factor)], [ r(factor), shape[0] - r(factor)], [shape[1] - r(factor),  r(factor)],
                       [shape[1] - r(factor), shape[0] - r(factor)]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, size)
    return dst

fo=open("uptrain.txt","w")
count=0
l=0
while count<10000:
    i = int(random.uniform(0, 10))
    j = int(random.uniform(0, 2))
    if i%10==0:
        if j==1:
            img = cv2.imread("D:\\doublenumber\\01.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s01.jpg")
        label=0.1
    if i%10==1:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\12.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s12.jpg")
        label=1.2
    if i%10==2:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\23.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s23.jpg")
        label=2.3
    if i%10==3:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\34.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s34.jpg")
        label=3.4
    if i%10==4:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\45.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s45.jpg")
        label=4.5
    if i%10==5:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\56.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s56.jpg")
        label=5.6
    if i%10==6:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\67.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s67.jpg")
        label=6.7
    if i%10==7:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\78.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s78.jpg")
        label=7.8
    if i%10==8:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\89.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s89.jpg")
        label=8.9
    if i%10==9:
        if j == 1:
            img = cv2.imread("D:\\doublenumber\\90.jpg")
        else:
            img = cv2.imread("D:\\doublenumber\\s90.jpg")
        label=9.0
    r_cropstart=int(random.uniform(16,40))
    imgcrop=img[r_cropstart:r_cropstart+74,0:39]
    imgcrop=tfactor(imgcrop)
    if count % 3 == 0:
        imgcrop = addNoise(imgcrop)
    imgcrop=AddGauss(imgcrop,3)
    imgcrop=cv2.resize(imgcrop,(39,75))
    cv2.imwrite("updata/"+str(count)+".jpg",imgcrop)
    fo.write(str(count)+".jpg"+" "+str(label)+"\n")
    count+=1
fo.close()
