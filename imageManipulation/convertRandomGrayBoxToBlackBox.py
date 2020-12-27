import cv2, numpy, os

blackImage = cv2.imread('/Users/Rich/RandomGray.png')
blackImage[:,:] = [0,0,0]
cv2.imwrite('/Users/Rich/RandomBlack.png', blackImage)
