# -*- coding: utf-8 -*-
import numpy as np
import urllib
import cv2

# img = cv2.imread('asset/pic2.jpg')
# print(img.shape)
# img_encode = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY),25])[1]
#
# data_encode = np.array(img_encode)
# str_encode = data_encode.tostring()
#
# # 缓存数据保存到本地，以txt格式保存
# with open('asset/img_encode.txt', 'wb') as f:
#     f.write(str_encode)
#
# with open('asset/img_encode.txt', 'rb') as f:
#     str_encode = f.read()
#
#
# image = np.asarray(bytearray(str_encode), dtype="uint8")
# img_decode = cv2.imdecode(image, cv2.IMREAD_COLOR)
#
#
# cv2.imshow('title', img_decode)
# cv2.waitKey(10000)



camera = cv2.VideoCapture(0)
while True:
    rec, img =  camera.read()
    img = cv2.resize(img,(128,128))
    cv2.imwrite('asset/{}.jpg'.format(img.shape),img)

    img_encode = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 25])[1]
    data_encode = np.array(img_encode)
    str_encode = data_encode.tostring()
    # 缓存数据保存到本地，以txt格式保存
    with open('asset/{}.txt'.format(img.shape), 'wb') as f:
        f.write(str_encode)

    cv2.imshow("title", img)
    cv2.waitKey(100)
