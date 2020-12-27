import cv2, numpy, os

blackImage = cv2.imread('/Users/Rich/RandomBlack.png')
blackImage[0,0] = [255, 255, 255]
cv2.imwrite('/Users/Rich/RandomWhiteDot.png', blackImage)
