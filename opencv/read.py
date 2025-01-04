import cv2 as cv

# #Reading Images
# img = cv.imread('Photos/group.jpeg')
# cv.imshow('Group Cat', img)

# cv.waitKey(0)

#Reading Videos
capture = cv.VideoCapture('Videos/game.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()