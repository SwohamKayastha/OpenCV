import cv2 as cv

img = cv.imread('Photos/group.jpeg')
cv.imshow('Group Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)


threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)