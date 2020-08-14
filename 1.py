import cv2
import numpy as np
import random

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

fo=open("datatrain.txt","w")
count=0
i=0
while count<30000:
    if i%17==0:
        img = cv2.imread("D:\\w1.jpg")
    if i%17==1:
        img = cv2.imread("D:\\w2.jpg")
    if i%17==2:
        img = cv2.imread("D:\\w16.jpg")
    if i%17==3:
        img = cv2.imread("D:\\w11.jpg")
    if i%17==4:
        img = cv2.imread("D:\\w3.jpg")
    if i%17==5:
        img = cv2.imread("D:\\w10.jpg")
    if i%17==6:
        img = cv2.imread("D:\\w15.jpg")
    if i%17==7:
        img = cv2.imread("D:\\w9.jpg")
    if i%17==8:
        img = cv2.imread("D:\\w8.jpg")
    if i%17==9:
        img = cv2.imread("D:\\w7.jpg")
    if i%17==10:
        img = cv2.imread("D:\\w17.jpg")
    if i%17==11:
        img = cv2.imread("D:\\w13.jpg")
    if i%17==12:
        img = cv2.imread("D:\\w12.jpg")
    if i%17==13:
        img = cv2.imread("D:\\w4.jpg")
    if i%17==14:
        img = cv2.imread("D:\\w14.jpg")
    if i%17==15:
        img = cv2.imread("D:\\w6.jpg")
    if i%17==16:
        img = cv2.imread("D:\\w5.jpg")
    r_cropstart = int(random.random() * (img.shape[0] - 60))
    #int(random.uniform(0, 10))

    # a=random.random()
    # print(a)
    # print(img.shape[0])
    if r_cropstart <= 40:
        if r_cropstart + 59 <= 76:
            label = 0
        else:
            label = 0.1
    if not (not (r_cropstart <= 100) or not (r_cropstart > 40)):
        if r_cropstart + 59 <= 126:
            label = 1
        else:
            label = 1.2
    if not (not (r_cropstart <= 155) or not (r_cropstart > 100)):
        if r_cropstart + 59 <= 185:
            label = 2
        else:
            label = 2.3
    if not (not (r_cropstart <= 215) or not (r_cropstart > 155)):
        if r_cropstart + 59 <= 242:
            label = 3
        else:
            label = 3.4
    if not (not (r_cropstart <= 265) or not (r_cropstart > 215)):
        if r_cropstart + 59 <= 300:
            label = 4
        else:
            label = 4.5
    if not (not (r_cropstart <= 323) or not (r_cropstart > 265)):
        if r_cropstart + 59 <= 356:
            label = 5
        else:
            label = 5.6
    if not (not (r_cropstart <= 380) or not (r_cropstart > 323)):
        if r_cropstart + 59 <= 410:
            label = 6
        else:
            label = 6.7
    if not (not (r_cropstart <= 435) or not (r_cropstart > 380)):
        if r_cropstart + 59 <= 470:
            label = 7
        else:
            label = 7.8
    if not (not (r_cropstart <= 493) or not (r_cropstart > 435)):
        if r_cropstart + 59 <= 525:
            label = 8
        else:
            label = 8.9
    if not (not (r_cropstart <= 548) or not (r_cropstart > 493)):
        if r_cropstart + 59 <= 583:
            label = 9
        else:
            label = 9.0
    if not (not (r_cropstart <= 623) or not (r_cropstart > 548)):
        if r_cropstart + 59 <= 623:
            label = 0
    imgcrop = img[r_cropstart:r_cropstart + 59, 0:39]
    if i%14==1:
        imgcrop = tfactor(imgcrop)
    if i%14==2:
        imgcrop = tfactor(imgcrop)
    if i%14==3:
        imgcrop = tfactor(imgcrop)
    if i%14==4:
        imgcrop = tfactor(imgcrop)
    if i%14==5:
        imgcrop = tfactor(imgcrop)
    if count % 3 == 0:
        imgcrop = addNoise(imgcrop)
    imgcrop = AddGauss(imgcrop, 3)
    imgcrop = cv2.resize(imgcrop, (39, 70))
    if count % 10 == 0:
        imgcrop = rotRandrom(imgcrop, 5, (39, 70))
        imgcrop = imgcrop[3:65, 3:35]
        imgcrop = cv2.resize(imgcrop, (39, 70))
    cv2.imwrite("data/" + str(count) + ".jpg", imgcrop)
    fo.write(str(count) + ".jpg" + " " + str(label) + "\n")
    count += 1
    i += 1
fo.close()
