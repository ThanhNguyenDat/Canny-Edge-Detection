import cv2
import numpy as np

cv2.namedWindow('Color Track Bar')


def nothing(x):
    pass


cv2.createTrackbar("Max", "Color Track Bar", 0, 255, nothing)
cv2.createTrackbar("Min", "Color Track Bar", 0, 255, nothing)

path = ''
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
while True:
    x = cv2.getTrackbarPos("Max", "Color Track Bar")
    y = cv2.getTrackbarPos("Min", "Color Track Bar")
    ret, thresh1 = cv2.threshold(blur, x, y, cv2.THRESH_BINARY)
    ret, thresh4 = cv2.threshold(blur, x, y, cv2.THRESH_TOZERO)

    cv2.imshow("thresh1", thresh1)
    cv2.imshow("thresh4", thresh4)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
