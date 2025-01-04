import cv2 as cv
import numpy as np

#Reading Images
img = cv.imread('Photos\gt.jpeg')
cv.imshow('Porsche', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([b, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blur', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)