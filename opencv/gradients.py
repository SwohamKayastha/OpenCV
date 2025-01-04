import cv2 as cv
import numpy as np

#Reading Images
img = cv.imread('Photos/gt.jpeg')
cv.imshow('Group Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx  = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely  = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_and(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel Combined', sobel_combined)

canny = cv.Canny(gray, 150, 255)
cv.imshow('Canny', canny)

canny2 = cv.Canny(canny, 150, 255)
cv.imshow('Canny 2', canny2)

cv.waitKey(0)
