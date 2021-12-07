import cv2
import numpy as np
import random


'''random generate img'''
# img = np.empty((300, 300, 3), np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


img = cv2.imread('dog.jpg')
cut_img = img[:150, :150]

cv2.imshow('img', img)
cv2.imshow('newImg', cut_img)
cv2.waitKey(0)
