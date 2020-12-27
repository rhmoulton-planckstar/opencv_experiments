import cv2, numpy, os

blackImage = cv2.imread('/Users/Rich/RandomBlack.png')
blackImage[0,0] = [255, 0, 0]
blackImage[0,1] = [0, 255, 0]
blackImage[0,2] = [0, 0, 255]
cv2.imwrite('/Users/Rich/NonRandomDots.png', blackImage)
