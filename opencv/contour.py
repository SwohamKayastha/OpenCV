import cv2 as cv
import numpy as np

img2 = cv.imread('Photos/group.jpeg')
# cv.imshow('Cats', img2)


def rescaleFrame(frame, scale=0.35):
    # Image , Videos and live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescaleFrame(img2)
cv.imshow('Image resized', img)


blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# # Blur
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('BLUR', blur)


# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawns', blank)

cv.waitKey(0)